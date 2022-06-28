from flask import Flask, jsonify, redirect, render_template, request
import json
import string
from random import choice


app = Flask(__name__)

# to open the url_storage.json if it blank than we assign it as empty dict.
with open("url_storage.json", "r") as f:
    try:
        url_storage = json.load(f)
    except:
        url_storage = {}


def generate_short_id(num_of_chars: int):
    """Function to generate short_id of specified number of characters"""
    return "".join(
        choice(string.ascii_letters + string.digits) for _ in range(num_of_chars)
    )


@app.route("/<path:long_url>", methods=["GET"])
def api_call(long_url):
    """this function takes one argument long_url and generates the short_url of it using random char.
        WORKING: this function will generate the short_id of every long url and it will be stored in the file
                 when agian endpoint is called with same long_url than it will return from the url_storage instead
                 of generating new one.
    ARGUMENT:
        long_url = long_url that to be shorten
    RETURN:
        shorten_url = shorter version of long url"""

    if long_url not in url_storage:
        try:
            short_id = generate_short_id(8)
            short_url = request.host_url + short_id
            url_storage[long_url] = short_id
            with open("url_storage.json", "w+") as f:
                f.write(json.dumps(url_storage))
            return {"shorten_url": short_url}
        except Exception as e:
            return {"error": e}
    else:
        try:
            host_url=request.host_url
        except:
            host_url="http://127.0.0.1:5000/"
        return {"shorten_url": host_url + url_storage[long_url]}


@app.route("/<short_id>", methods=["GET"])
def redirect_url(short_id):
    """this function is called when /<short_id> endpoint is called
        working : when short_id is present in the values of url_storage than it will redirected to the particular key
                  related to that short_id else it will return the error message.
    ARGUMENTS:
        short_id : short_id of a long_url
    RETURN:
        json object with "error" key when short_id is not present in the url_storage"""
    if short_id in url_storage.values():
        return redirect(
            list(url_storage.keys())[list(url_storage.values()).index(short_id)]
        )
    else:
        return {"error": "need to generate short_url first"}


if __name__ == "__main__":
    app.run(debug=True)
