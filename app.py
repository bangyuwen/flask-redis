import redis
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/redis-cache')
def redis_cache():
    number = request.args.get('no')
    if not number:
        return 'Please give no query parameter'
    result = redis_client.get(number)
    if not result:
        result = str(datetime.utcnow())
        redis_client.set(number, result)
    return result
