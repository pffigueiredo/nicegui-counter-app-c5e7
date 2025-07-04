from pydantic import BaseModel, Field
from typing import Optional


class CounterCreate(BaseModel):
    name: str = Field(..., max_length=100, description="Name of the counter")
    value: int = Field(default=0, description="Initial value of the counter")


class CounterUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100, description="Name of the counter")
    value: Optional[int] = Field(None, description="New value of the counter")


class CounterResponse(BaseModel):
    id: int
    name: str
    value: int
    created_at: str
    updated_at: str