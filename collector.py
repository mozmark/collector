from flask import Flask, request
from datetime import datetime
from elasticsearch import Elasticsearch
import messages

es = Elasticsearch()

app = Flask(__name__)

def log_success(msg):
    pass

def log_failure(msg):
    print 'failure: %s' % (msg)

@app.route('/v1', methods=['POST'])
def index():
    try:
        json = request.json
        if None != json:
            if messages.is_valid(json, messages.v1()):
                es.index(index="ssl_errors", doc_type="pin error", body=json)
            else:
                log_failure('document not valid')
        else:
            log_failure('bad request')
    except Exception as e:
        print e
    return 'OK'

if __name__ == '__main__':
    app.run()
