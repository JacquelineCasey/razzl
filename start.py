
from flask import Flask

app = Flask(__name__)

sockets = Sockets(app)
redis = redis.from_url(REDIS_URL)


@app.route('/')
def hello():
    app.send_static_file('index.html')
