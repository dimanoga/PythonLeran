import enum

import sqlalchemy as sa
import sqlalchemy_utils as su

from payment_reminders.db import Base


class ReminderType(str, enum.Enum):
    p2p = 'p2p'
    mobile = 'mobile'
    template = 'template'


class Reminders(Base):
    __tablename__ = 'reminders'

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    party_id = sa.Column(sa.Text, nullable=False)
    reminder_type = sa.Column(
        su.ChoiceType(ReminderType, impl=sa.Text()),
        nullable=False,
        doc='Тип напоминания',
    )
    predicted_payment_dt = sa.Column(sa.Date)
    predicted_payment_amt = sa.Column(sa.FLOAT)
    phone_number = sa.Column(sa.Text)
    name = sa.Column(sa.Text)
    time_zone_cd = sa.Column(sa.FLOAT)
    template_id = sa.Column(sa.INT)
