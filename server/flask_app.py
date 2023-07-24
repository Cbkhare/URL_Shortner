import requests
from resources import db, url_shortner

from flask import Flask, make_response

app = Flask(__name__)


db_conn = db.URLShornterDBAcess(db.DB())

@app.route('/create', methods=['GET'])
def create():
    msg = ""
    status_code = 400  # default code 
    try:
        payload = requests.get_json()
        if "url" not in payload or payload["url"] == "":
            raise Exception("valid url not found")
        status_code = 201
        db_conn.insert(long_url=payload["url"],
                       short_url=url_shortner.generate_short_url(
            long_url=payload["url"])
        )
        msg = {"short_url": db_conn.get(long_url=payload["url"])}
        status_code = 201
    except Exception as e: 
        msg = e 
        status_code = 500
    return make_response(msg, status_code)


@app.route('/get', methods=['GET'])
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/delete', methods=['DELETE'])
def hello():
    return '<h1>Hello, World!</h1>'


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)