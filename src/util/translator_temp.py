from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from typing import Tuple
import time
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")


class Translator:
    _model: AutoModelForSeq2SeqLM
    _tokenizer: AutoTokenizer

    def __init__(self) -> None:
        self._model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
        self._tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
    
    def translate(self, text: str, tgt_lang: str, src_lang: str = "en_Latn") -> Tuple[bool, str]:
        try:
            self._tokenizer.src_lang = src_lang
            encoder = self._tokenizer(text, return_tensors="pt")
            generated_tokens = self._model.generate(**encoder, forced_bos_token_id=self._tokenizer.lang_code_to_id[tgt_lang])
            return True, self._tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        except Exception as e:
            return False, str(e)
    
    def translate_batch(self, texts: list[str], tgt_lang: str, src_lang: str = "en_Latn") -> Tuple[bool, list[str] | str]:
        try:
            self._tokenizer.src_lang = src_lang
            encoder = self._tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
            generated_tokens = self._model.generate(**encoder, forced_bos_token_id=self._tokenizer.lang_code_to_id[tgt_lang])
            return True, self._tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        except Exception as e:
            return False, str(e)

def benchmark():
    single_text = "Hello, how are you?"
    batch = ["Hello, how are you?", "I am fine, thank you."]
    oth_text = "हैलो, आप कैसे हैं?"
    print("Starting Time Benchmark")
    start = time.time()
    print("Creating Translator Instance")
    t = Translator()
    ans = t.translate(single_text, "hin_Deva")
    end = time.time()
    print(ans)
    print(f"Time Taken for single Translation: {end - start} seconds")

    start2 = time.time()
    t = Translator()
    ans = t.translate_batch(batch, "hin_Deva")
    end2 = time.time()
    print(ans)
    print(f"Time Taken for batch Translation: {end2 - start2} seconds")
    
    start3 = time.time()
    t = Translator()
    ans = t.translate(oth_text, "en_Latn", "hin_Deva")
    end3 = time.time()
    print(ans)
    print(f"Time Taken for other language to English Translation: {end3 - start3} seconds")

if __name__ == '__main__':
    benchmark()
    print("Done!")