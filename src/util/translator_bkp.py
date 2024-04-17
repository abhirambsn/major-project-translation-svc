from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
import time

class Translator:
    _model: M2M100ForConditionalGeneration
    _tokenizer: M2M100Tokenizer

    def __init__(self) -> None:
        self._model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
        self._tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
    
    def translate(self, text: str, tgt_lang: str, src_lang: str = "en") -> str:
        self._tokenizer.src_lang = src_lang
        encoder = self._tokenizer(text, return_tensors="pt")
        generated_tokens = self._model.generate(**encoder, forced_bos_token_id=self._tokenizer.get_lang_id(tgt_lang))
        return self._tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    
    def translate_batch(self, texts: list[str], tgt_lang: str, src_lang: str = "en") -> list[str]:
        self._tokenizer.src_lang = src_lang
        encoder = self._tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
        generated_tokens = self._model.generate(**encoder, forced_bos_token_id=self._tokenizer.get_lang_id(tgt_lang))
        return self._tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

print("Starting Time Benchmark")
start = time.time()
print("Creating Translator Instance")
t = Translator()
ans = t.translate("Hello, how are you?", "fr")
end = time.time()
print(ans)
print(f"Time Taken for single Translation: {end - start} seconds")
start2 = time.time()
ans = t.translate_batch(["Hello, how are you?", "I am fine, thank you."], "hi")
end2 = time.time()
print(ans)
print(f"Time Taken for batch Translation: {end2 - start2} seconds")