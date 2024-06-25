import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk


# service for endpoints functionality (using ntkl)
class NTKLService:
    def __init__(self) -> None:
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')
    
    async def tokenize_text(self, text: str):
        return word_tokenize(text)
    
    async def pos_tag_text(self, text: str):
        tokens = word_tokenize(text)
        return pos_tag(tokens)

    async def ner_text(self, text: str):
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        named_entities = ne_chunk(pos_tags)
        return named_entities