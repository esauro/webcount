from flask import Flask
from flask import request
from parser.webtokenizer import BSTokenizer
import json

app = Flask(__name__)


@app.route('/api/', methods=["POST"])
def counter():
    tokenizer = BSTokenizer(request.form["url"])

    return json.dumps(tokenizer.get_most_common_words(100))


if __name__ == '__main__':
    app.run()
