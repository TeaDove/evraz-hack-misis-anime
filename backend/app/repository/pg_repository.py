from dataclasses import dataclass

from sqlalchemy import Column, DateTime, Integer, create_engine, literal_column
from sqlalchemy.dialects.postgresql import JSONB, insert
from sqlalchemy.orm import Session, declarative_base

from schemas.event import ExhausterEvent
from shared.base import logger
from shared.settings import app_settings

Base = declarative_base()


class PGEvent(Base):
    __table_args__ = {"schema": "public"}
    __tablename__ = "event"

    id = Column(Integer(), primary_key=True)
    created_at = Column(DateTime(timezone=True))
    exhauster_id = Column(Integer)
    status = Column(JSONB)


@dataclass
class PGRepository:
    def __post_init__(self):
        self.engine = create_engine(
            f"postgresql+psycopg2://{app_settings.pg_username}:{app_settings.pg_password}@"
            f"{app_settings.pg_host}:{app_settings.pg_port}/{app_settings.pg_database}"
        )

    def insert_event(self, event: ExhausterEvent):
        with Session(self.engine) as session:
            statement = (
                insert(PGEvent)
                .values(
                    created_at=event.created_at,
                    exhauster_id=event.exhauster_id,
                    status=event.status.jsonable_dict(),
                )
                .on_conflict_do_nothing()
                .returning(literal_column("*"))
            )
            result = session.execute(statement)
            if result is None:
                logger.exception("duplicated.key")
                session.rollback()
            session.commit()
