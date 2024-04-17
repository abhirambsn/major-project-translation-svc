from repository import TranslatorRepository
from typing import Tuple
from dtypes import TranslateRequest

class TranslatorService:
    _repository: TranslatorRepository

    def __init__(self, repo: TranslatorRepository) -> None:
        self._repository = repo

    def process_translation_request(self, request: TranslateRequest) -> Tuple[bool, str | list[str] | None, float | None]:
        try:
            text, time = self._repository.translate(request.text, request.tgt_lang, request.src_lang)
            return True, text, time
        except Exception as _:
            return False, None, None
    