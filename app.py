from flask import Flask
from flask import json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    ## Log implementation
    app.logger.info('Main request successfull')
    return "Hello World! From Python"

@app.route('/status')
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    ## Log implementation
    app.logger.info('Status request successfull')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserActive":23}}),
        status=200,
        mimetype='application/json'
    )
    ## Log implementation
    app.logger.info('Matrics request successfull')
    return response


if __name__ == "__main__":

    ## stream logs to app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0', port=8080)
