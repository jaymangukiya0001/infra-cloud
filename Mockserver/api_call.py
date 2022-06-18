import bitly_api
from flask import Flask, jsonify, redirect, render_template
import json


app = Flask(__name__)
auth_token = "0ad359081ec6cced83ddfad9626d7ffd35c827ba"

# to open the url_storage.json if it blank than we assign it as empty dict.
with open("url_storage.json", "r") as f:
    try:
        url_storage = json.load(f)
    except:
        url_storage = {}


@app.route("/api_call/<path:long_url>", methods=["GET"])
def api_call(long_url):
    """this function takes one argument and calls bitly api and returns a shorten URL of long_url
    ARGUMENT:
        long_url = long_url that to be shorten
    RETURN:
        shorten_url = shorter version of long url"""
    if long_url not in url_storage:
        try:
            connection = bitly_api.Connection(access_token=auth_token)
            shorten_url = connection.shorten(long_url)
            url_storage[long_url] = shorten_url["url"]
            with open("url_storage.json", "w+") as f:
                f.write(json.dumps(url_storage))
            return {"shorten_url": shorten_url["url"]}
        except Exception as e:
            return {"error":e}
    else:
        return {"shorten_url": url_storage[long_url]}


if __name__ == "__main__":
    app.run(debug=True)
