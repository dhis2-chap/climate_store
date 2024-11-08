from typing import Optional, Literal
from sqlmodel import SQLModel, Field

Aggregation = Literal["mean", "sum", "median", "min", "max"]

class ClimateAggregate(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    location: str = Field(index=True)
    period: str = Field(index=True)
    band: str
    temporal_aggregation: Aggregation
    spatial_aggregation: Aggregation
    value: float


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)


