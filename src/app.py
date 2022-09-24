from flask import Flask
from manifest import parse

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ipfs_hash/<ipfs_hash>")
def get_manifest_data(ipfs_hash: str):
    manifest = parse(ipfs_hash)
    data = []
    for source in manifest.data_sources:
        data.append({
            "kind": source.kind,
            "mapping": source.mapping,
            "name": source.name,
            "network": source.network,
            "source": source.source
        })
    return data


