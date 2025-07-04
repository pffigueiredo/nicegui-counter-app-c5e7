from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class Counter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, unique=True)
    value: int = Field(default=0)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    def increment(self) -> int:
        """Increment the counter value by 1 and return the new value."""
        self.value += 1
        self.updated_at = datetime.utcnow()
        return self.value

    def decrement(self) -> int:
        """Decrement the counter value by 1 and return the new value."""
        self.value -= 1
        self.updated_at = datetime.utcnow()
        return self.value

    def reset(self) -> int:
        """Reset the counter value to 0 and return the new value."""
        self.value = 0
        self.updated_at = datetime.utcnow()
        return self.value