from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from base_sqlalchemy import Base


class MChildChild(Base):
    __tablename__ = "mchildchild"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    def __eq__(self, other: MChildChild): # type: ignore
        return self.id == other.id