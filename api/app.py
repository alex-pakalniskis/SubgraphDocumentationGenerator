from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<schema>")
def make_docs(ipfs_hash: str):
    return ipfs_hash