

import sqlalchemy.orm as so
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from contextlib import contextmanager

from sqlAlchemy.Reminders import Reminders

metadata = MetaData()

Base = declarative_base(metadata=metadata)

Session = so.sessionmaker()
current_session = so.scoped_session(Session)


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
