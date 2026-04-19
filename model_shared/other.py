from datetime import datetime

from sqlalchemy import UUID, text, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ModelBase(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(UUID,
                                     primary_key=True,
                                     server_default=text("gen_random_uuid()"),
                                     comment="id")

class TimeMixin(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment="created_at")
    edited_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment="edited_at")
