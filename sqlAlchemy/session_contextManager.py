import sqlalchemy.orm as so
from pydantic import BaseSettings
from sqlalchemy import MetaData, engine_from_config
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base
from contextlib import contextmanager

from sqlalchemy.pool import SingletonThreadPool, Pool

from sqlAlchemy.Reminders import Reminders

metadata = MetaData()

Base = declarative_base(metadata=metadata)

Session = so.sessionmaker()
current_session = so.scoped_session(Session)


class DBSettings(BaseSettings):
    url = 'postgresql://oleg:oleg_pass@localhost:5433'
    connection_timeout: int = 30
    pool_timeout: int = 5
    pool_pre_ping: bool = True
    pool_recycle: int = 500
    pool_size: int = 6
    poolclass: Pool = SingletonThreadPool
    echo: bool = False

    class Config:
        env_prefix = 'DB_'

    def setup_db(self) -> None:

        metadata.bind = self.create_engine(url=self.url)

    def create_engine(self, url: str) -> Engine:
        return engine_from_config(
            {
                'url': url,
                "pool_recycle": self.pool_recycle,
                "pool_pre_ping": self.pool_pre_ping,
                "pool_size": self.pool_size,
                "poolclass": self.poolclass,
                "connect_args": {'connect_timeout': self.connection_timeout},
            },
            prefix="",
        )


@contextmanager
def create_session(expire_on_commit: bool = True) -> Iterator[so.Session]:
    """Provide a transactional scope around a series of operations."""
    new_session = Session(expire_on_commit=expire_on_commit)
    try:
        yield new_session
        new_session.commit()
    except Exception:
        new_session.rollback()
        raise
    finally:
        new_session.close()


with create_session() as session:
    with create_session() as session:
        session.query(Reminders).filter(Reminders.party_id == 'smth').update(
            {Reminders.party_id: 'smth'}
        )
