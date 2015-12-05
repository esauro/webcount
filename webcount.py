from flask import Flask
from flask import request
from flask import abort
from parser.webtokenizer import BSTokenizer
import json


app = Flask(__name__)


@app.route('/api/', methods=["POST"])
def counter():
    if (request.form["site"] is None) or (request.form["site"] == ""):
        return abort(400)
    tokenizer = BSTokenizer(request.form["site"])
    return json.dumps(tokenizer.get_most_common_words(100))


if __name__ == '__main__':
    app.run()
