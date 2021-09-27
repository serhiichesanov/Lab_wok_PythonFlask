from flask import Flask

app = Flask(__name__)

@app.route("/api/v1/hello-world-14")
def hello_world():
    return "Hello world 14"
