from flask import Flask
from manifest import parse

app = Flask(__name__)

@app.route("/ipfs_hash/<ipfs_hash>")
def get_manifest_data(ipfs_hash: str):
    manifest = parse(ipfs_hash)
    data = {}
    for i in range(len(manifest.data_sources)):
        data[i] = {}
        data[i]["kind"] = manifest.data_sources[i].kind
        data[i]["mapping"] = manifest.data_sources[i].mapping
        data[i]["name"] = manifest.data_sources[i].name
        data[i]["network"] = manifest.data_sources[i].network
        data[i]["source"] = manifest.data_sources[i].source
    return data


