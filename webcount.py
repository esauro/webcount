# -*- coding: utf-8 -*-
"""This is the API to perform web word counting."""
import json

from flask import Flask
from flask import abort
from flask import request

from webtokenizer import BSTokenizer


app = Flask(__name__)


@app.route('/api/', methods=["POST"])
def counter():
    """
        * Receive request
        * If the request have "site" and is None or empty string:
            * Return BadRequest (HttpErrorCode 400)
        * Else
            * Call tokenizer
            * Convert to JSON

        Returns:
            A JSON string containing a list of words and repetitions. ex '[["to", 30],["the",29]]'
    """

    if (request.form["site"] is None) or (request.form["site"] == ""):
        return abort(400)
    tokenizer = BSTokenizer(request.form["site"])
    return json.dumps(tokenizer.get_most_common_words(100))


if __name__ == '__main__':
    app.run()