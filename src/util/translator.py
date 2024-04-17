from ctranslate2 import Translator as CTranslator
from transformers.models.nllb.tokenization_nllb_fast import NllbTokenizerFast
from pathlib import Path
import time
from typing import Tuple


class Translator:
    tokenizer: NllbTokenizerFast
    translator: CTranslator

    
    def __init__(self):
        model_path = str(Path(__file__).parent.parent.parent / "nllb-pretrained-ckpt")

        self.translator = CTranslator(model_path)
        self.tokenizer = NllbTokenizerFast.from_pretrained("facebook/nllb-200-distilled-600M")

    def translate(self, text: str, src_lang_code: str, tgt_lang_code: str) -> Tuple[str | list[str], float]:
        self.tokenizer.src_lang = src_lang_code

        start = time.time()

        source = [self.tokenizer.convert_ids_to_tokens(self.tokenizer.encode(line)) for line in text.splitlines() if line.strip()]
        target_prefix = [tgt_lang_code]

        results = self.translator.translate_batch(source, target_prefix=[target_prefix])
        target = results[0].hypotheses[0][1:]

        output = self.tokenizer.decode(self.tokenizer.convert_tokens_to_ids(target))

        stop = time.time()
        return output, round(stop - start, 2)
