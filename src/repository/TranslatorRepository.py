from util import Translator
from typing import Tuple
from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

class TranslatorRepository:
    def __init__(self, translator: Translator = Translator()):
        self._translator = translator
    
    def translate(self, text: str, tgt_lang: str, src_lang: str = "en_Latn") -> Tuple[str | list[str], float]:
        try:
            result = self._translator.translate(text, src_lang, tgt_lang)
        except KeyError as exc:
            raise HTTPException(HTTP_400_BAD_REQUEST, "Invalid Language code") from exc
        
        if not result:
            raise HTTPException(HTTP_400_BAD_REQUEST, "Translation failed")
        
        return result