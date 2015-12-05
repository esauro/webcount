from flask import Flask
from parser.webtokenizer import BSTokenizer

app = Flask(__name__)


@app.route('/')
def hello_world():
    tokenizer = BSTokenizer("https://bbc.co.uk")
    return repr(tokenizer.get_most_common_words(10))


if __name__ == '__main__':
    app.run()
