from typing import Optional
from sqlalchemy import Integer, String, Time, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from database.config import Base, engine


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[String] = mapped_column(String)
    description_short: Mapped[String] = mapped_column(String)
    description_md: Mapped[String] = mapped_column(String)
    is_public: Mapped[Boolean] = mapped_column(Boolean)

    creator: Mapped[String] = mapped_column(String, index=True, nullable=True)

    # Metadata
    created_at: Mapped[Optional[Time]] = mapped_column(Time)
    updated_at: Mapped[Optional[Time]] = mapped_column(Time)
    deleted_at: Mapped[Optional[Time]] = mapped_column(Time, nullable=True)


Base.metadata.create_all(engine)
