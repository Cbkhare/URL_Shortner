import db 
import json
from url_shortner import generate_short_url
 
from flask import Flask, request

app = Flask(__name__)

db_conn = db.URLShornterDBAcess(db.DB())

@app.route('/create', methods=['POST'])
def create_url():
    msg = ""
    status_code = 400  # default code 
    try:
        payload = json.loads(request.data)
        if "url" not in payload or payload["url"] == "":
            raise Exception("valid url not found")
        status_code = 201
        db_conn.insert(long_url=payload["url"],
                       short_url=generate_short_url(
            long_url=payload["url"])
        )
        msg = {"short_url": db_conn.get(long_url=payload["url"])}
        status_code = 201
    except Exception as e: 
        msg = str(e) 
        status_code = 500
    return json.dumps({"msg": msg, "status_code": status_code})


@app.route('/get', methods=['GET'])
def get_url():
    msg = ""
    status_code = 400  # default code 
    try:
        payload = json.loads(request.data)
        if "url" not in payload or payload["url"] == "":
            raise Exception("valid url not found")
        short_url = db_conn.get(long_url=payload["url"])
        if short_url:
            status_code = 201
            msg = {"short_url": short_url, msg: ""}
        else:
            status_code = 401
            msg = {"short_url": "", msg: "short url not found."}
    except Exception as e: 
        msg = str(e) 
        status_code = 500
    return json.dumps({"msg": msg, "status_code": status_code})


@app.route('/delete', methods=['DELETE'])
def delete_url():
    msg = ""
    status_code = 400  # default code 
    try:
        payload = json.loads(request.data)
        if "url" not in payload or payload["url"] == "":
            raise Exception("valid url not found")
        msg = db_conn.delete(long_url=payload["url"])
        status_code = 201
    except Exception as e: 
        msg = str(e) 
        status_code = 500
    return json.dumps({"msg": msg, "status_code": status_code})

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)