from .response import ApiResponse
from .requests import TranslateRequest
from fastapi import Response, WebSocket
from typing import Optional, TypeVar

T = TypeVar('T')

def make_response(response: Response, status: int, message: Optional[str] = None, data: Optional[T] = None) -> dict:
    response.status_code = status
    return ApiResponse.APIResponse(status=status, message=message, data=data).to_dict()

async def make_ws_response(ws: WebSocket, status: int, message: Optional[str] = None, data: Optional[T] = None) -> dict:
    await ws.send_json(ApiResponse.APIResponse(status=status, message=message, data=data).to_dict())