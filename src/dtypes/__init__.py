from .response import ApiResponse
from .requests import TranslateRequest
from fastapi import Response
from typing import Optional, TypeVar

T = TypeVar('T')

def make_response(response: Response, status: int, message: Optional[str] = None, data: Optional[T] = None) -> dict:
    response.status_code = status
    return ApiResponse.APIResponse(status=status, message=message, data=data).to_dict()