from typing import TypeVar, Generic, Optional
from pydantic import BaseModel

T = TypeVar('T')


class APIResponse(BaseModel, Generic[T]):
    status: int = 200
    message: Optional[str] = None
    data: Optional[T] = None

    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "message": self.message,
            "data": self.data
        }