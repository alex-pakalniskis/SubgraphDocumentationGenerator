from flask import Flask

from classes import ManifestOutput
from utils import parse_yml, parse_graphql


app = Flask(__name__)

# Basically a test route that will get deleted eventually once make_docs route is complete
@app.route("/ipfs_hash/<ipfs_hash>")
def get_manifest_data(ipfs_hash: str):
    manifest: ManifestOutput = parse_yml(ipfs_hash)
    data = {}
    for i in range(len(manifest.data_sources)):
        data[i] = {}
        data[i]["kind"] = manifest.data_sources[i].kind
        data[i]["mapping"] = manifest.data_sources[i].mapping
        data[i]["name"] = manifest.data_sources[i].name
        data[i]["network"] = manifest.data_sources[i].network
        data[i]["source"] = manifest.data_sources[i].source
    return data

@app.route("/docs/<ipfs_hash>")
def make_docs(ipfs_hash: str):
    manifest: ManifestOutput = parse_yml(ipfs_hash)
    schema = parse_graphql(manifest.schema_hash)
    return f"It's still a work in progress, {manifest.schema_hash}"



