class TranslateRequest:
    text: str | list[str]
    tgt_lang: str
    src_lang: str = "eng_Latn"

    def __init__(self, text: str | list[str], tgt_lang: str, src_lang: str = "eng_Latn"):
        self.text = text
        self.tgt_lang = tgt_lang
        self.src_lang = src_lang
    
    @staticmethod
    def from_json(json_data: dict):
        return TranslateRequest(
            text=json_data["text"],
            tgt_lang=json_data["tgt_lang"],
            src_lang=json_data.get("src_lang", "eng_Latn")
        )
    
    def to_json(self):
        return {
            "text": self.text,
            "tgt_lang": self.tgt_lang,
            "src_lang": self.src_lang
        }
    