import bitly_api
from flask import Flask, jsonify, redirect, render_template
import json


app = Flask(__name__)
auth_token = "0ad359081ec6cced83ddfad9626d7ffd35c827b"


@app.route("/api_call/<path:long_url>", methods=["GET"])
def api_call(long_url):
    """this function takes one argument and calls bitly api and returns a shorten URL of long_url
    ARGUMENT:
        long_url = long_url that to be shorten
    RETURN:
        shorten_url = shorter version of long url"""

    connection = bitly_api.Connection(access_token=auth_token)
    shorten_url = connection.shorten(long_url)
    return {"shorten_url": shorten_url["url"]}


if __name__ == "__main__":
    app.run(debug=True)
