from fastapi import APIRouter, Response, WebSocket, WebSocketDisconnect
from service import TranslatorService
from repository import TranslatorRepository
from dtypes import TranslateRequest, make_response, make_ws_response
from util import WsConnectionManager

router = APIRouter(prefix="/api/v1/translate", tags=["Translator"])

service = TranslatorService(
    repo=TranslatorRepository()
)

conn_manager = WsConnectionManager()

@router.get("/healthz")
async def perform_healthz_check(response: Response):
    return make_response(response, status=200, message="Healthy", data=None)

@router.websocket("/")
async def translate(websocket: WebSocket):
    await conn_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            req = TranslateRequest.from_json(data)
            success, text, time = service.process_translation_request(req)
            if not success:
                await make_ws_response(websocket, status=400, message="Translation failed", data=None)
            await make_ws_response(websocket, status=200, message="Translation successful", data={
                "text": text,
                "time": time
            })
    except WebSocketDisconnect:
        conn_manager.disconnect(websocket)
    