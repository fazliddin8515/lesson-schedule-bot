from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lesson_name: Mapped[str] = mapped_column(String(20), nullable=False)
    day_name: Mapped[str] = mapped_column(String(15), nullable=False)
    lesson_order: Mapped[int] = mapped_column(nullable=False)
