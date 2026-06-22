from pydantic import BaseModel
from datetime import datetime


class LogEntry(BaseModel):
    timestamp: datetime | None
    level: str
    ip: str | None
    message: str
    raw: str