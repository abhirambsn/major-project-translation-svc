from fastapi import APIRouter, Response, Depends
from service import TranslatorService
from repository import TranslatorRepository
from dtypes import TranslateRequest, make_response

router = APIRouter(prefix="/api/v1/translate", tags=["Translator"])

service = TranslatorService(
    repo=TranslatorRepository()
)

@router.get("/healthz")
async def perform_healthz_check(response: Response):
    return make_response(response, status=200, message="Healthy", data=None)

@router.post("/")
async def translate(req: TranslateRequest, response: Response):
    success, text, time = service.process_translation_request(req)
    if not success:
        return make_response(response, status=400, message="Translation failed", data=None)
    return make_response(response, status=200, message="Translation successful", data={
        "text": text,
        "time": time
    })
    