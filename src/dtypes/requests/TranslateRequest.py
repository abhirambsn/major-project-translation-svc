from pydantic import BaseModel

class TranslateRequest(BaseModel):
    text: str | list[str]
    tgt_lang: str
    src_lang: str = "eng_Latn"
    