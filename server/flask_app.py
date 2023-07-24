import db 
import json
from url_shortner import generate_short_url
 
from flask import Flask, request

app = Flask(__name__)

# Common DB connection for the flask app
db_conn = db.URLShornterDBAcess(db.DB())

@app.route('/create', methods=['POST'])
def create_url():
    """
    This method creates the short url for the given long url
    in the payload. 
    return: 
        msg: String, Message of the execution
        status_code: status code of the http api
    """
    msg = ""
    status_code = 400  # default code 
    try:
        # fetch the data
        payload = json.loads(request.data)
        if "url" not in payload or payload["url"] == "":
            raise Exception("valid url not found")
        
        # insert the short_url into the db 
        db_conn.insert(long_url=payload["url"],
                       short_url=generate_short_url(
            long_url=payload["url"])
        )
        # prepare message 
        msg = {"short_url": db_conn.get_short_url(long_url=payload["url"])}
        status_code = 201
    except Exception as e: 
        msg = str(e) 
        status_code = 500
    return json.dumps({"msg": msg, "status_code": status_code})


@app.route('/getShortUrl', methods=['GET'])
def get_url():
    """
    This method fetches the short url for the given long url.
    It is necessary that the short URL should be generated 
    before fetching the short url.
    returns:
        msg: String, Message of the execution. This also has the details
        of the short URL. 
        status_code: status code of the execution. """
    msg = ""
    status_code = 400  # default code 
    try:
        payload = json.loads(request.data)
        if "url" not in payload or payload["url"] == "":
            raise Exception("valid url not found")
        short_url = db_conn.get_short_url(long_url=payload["url"])
        if short_url:
            status_code = 201
            msg = {"short_url": short_url, msg: ""}
        else:
            status_code = 401
            msg = {"short_url": "", "msg": "short url not found."}
    except Exception as e: 
        msg = str(e) 
        status_code = 500
    return json.dumps({"msg": msg, "status_code": status_code})

@app.route('/getLongUrl', methods=['GET'])
def get_long_url():
    """
    This method fetches the long url for the given short url.
    It is necessary that the short URL should be generated 
    before fetching the long url.
    returns:
        msg: String, Message of the execution. This also has the details
        of the Long URL. 
        status_code: status code of the execution. 
    """
    msg = ""
    status_code = 400  # default code 
    try:
        payload = json.loads(request.data)
        if "url" not in payload or payload["url"] == "":
            raise Exception("valid url not found")
        long_url = db_conn.get_long_url(short_url=payload["url"])
        if long_url:
            status_code = 201
            msg = {"long_url": long_url, "msg": ""}
        else:
            status_code = 401
            msg = {"short_url": "", "msg": "short url not found."}
    except Exception as e: 
        msg = str(e) 
        status_code = 500
    return json.dumps({"msg": msg, "status_code": status_code})

@app.route('/delete', methods=['DELETE'])
def delete_url():
    """
    This method deletes the entry of the long and short URL details 
    from the db schema.
    returns:
        msg: String, Message of the execution. 
        status_code: status code of the execution. 
    """
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