from flask import Flask, request, jsonify, abort
from services.nlp import get_sentences, get_tokens_and_frequencies
import settings

app = Flask(__name__)
app.config.from_object(settings.DevelopmentConfig)

@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400
app.register_error_handler(400, bad_request)

@app.route("/")
def index():
    return "Hello Natalia!"

@app.route("/tokens", methods=["POST"])
def tokenizer():
    text = request.json.get("text")
    if not text:
        return abort(400)
    language = request.json.get("language") \
        if request.json.get("language") else "english"
    more_words = request.json.get("stopwords") \
        if request.json.get("stopwords") else []
    number = request.json.get("number")
    tokens = get_tokens_and_frequencies(text, language, more_words, number)
    return jsonify(tokens)

@app.route("/sentences", methods=["POST"])
def sentences():
    text = request.json.get("text")
    if not text:
        return abort(400)
    sentences = get_sentences(text)
    return jsonify(sentences)

if __name__ == "__main__":
    app.run()