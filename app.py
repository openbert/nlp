import json
import spacy
from flask import Flask, request, Response

nlp = spacy.load('de_core_news_md')
app = Flask(__name__)

@app.route('/', methods=['POST'])
def name_entities():
    nerRequest = request.get_json()

    nerResponse = {
        "entities": []
    }

    doc = nlp(nerRequest["text"])
    for ent in doc.ents:
        nerResponse["entities"].append({
            "name": ent.text,
            "label": ent.label_,
            "startChar": ent.start_char,
            "endChar": ent.end_char,
        })

    return Response(json.dumps(nerResponse), mimetype="application/json")

@app.route('/health', methods=['GET'])
def health():
    return 'ok'
