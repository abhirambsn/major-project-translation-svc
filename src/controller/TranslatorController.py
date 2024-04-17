from fastapi import APIRouter, Response, Depends
from service import TranslatorService
from repository import TranslatorRepository
from dtypes import TranslateRequest, make_response

router = APIRouter(prefix="/api/v1/translator", tags=["Translator"])

service = TranslatorService(
    repo=TranslatorRepository()
)

@router.post("/")
async def translate(req: TranslateRequest, response: Response):
    success, text, time = service.process_translation_request(req)
    if not success:
        return make_response(response, status=400, message="Translation failed", data=None)
    return make_response(response, status=200, message="Translation successful", data={
        "text": text,
        "time": time
    })
    