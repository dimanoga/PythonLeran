from pydantic import BaseModel


class Reminder(BaseModel):
    reminder_type: 'smth'
    party_id: str
    time_zone_cd: float
    predicted_payment_amt: Optional[float] = None
    phone_number: Optional[str] = None
    name: Optional[str] = None
    template_id: Optional[int] = None

    @validator('name', 'template_id')
    def check_required_name(
            cls, v: Optional[str], values: Dict[str, Any]
    ) -> Optional[str]:
        if values.get('reminder_type') == ReminderType.template and v is None:
            raise ValueError
        return v

    @validator('phone_number')
    def check_required_phone_number(
            cls, v: Optional[str], values: Dict[str, Any]
    ) -> Optional[str]:
        if (
                values.get('reminder_type') == ReminderType.mobile
                or values.get('reminder_type') == ReminderType.p2p
        ) and v is None:
            raise ValueError
        return v