from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import regexp_tokenize, sent_tokenize
from utils.stopwords import STOPSTRING

def _get_stopwords(language, more_words):
    return stopwords.words(language) \
        + STOPSTRING \
        + list(more_words)

def _get_tokens(text, stopwords):
    words = regexp_tokenize(text.lower(), '\w+')
    return [w for w in words if w not in stopwords]

def _get_frequencies(tokens, number):
    if number:
        return FreqDist(tokens).most_common(number)
    return FreqDist(tokens).most_common()

def get_tokens_and_frequencies(text, language, more_words, number):
    stopwords = _get_stopwords(language, more_words)
    tokens = _get_tokens(text, stopwords)
    f = _get_frequencies(tokens, number)
    return [{'word': word, 'frequency': frequency} for word, frequency in f]

def get_sentences(text):
    sentences = sent_tokenize(text)
    numbers = (x for x in range(0, len(sentences)))
    return [{'text': s, 'number': next(numbers)} for s in sentences]