# from calendar import month_name
from flask import Flask

from classes import ManifestOutput, SchemaOutput, OverviewPage
from utils import parse_yml, parse_gql, manifest_output_to_json


app = Flask(__name__)

@app.route("/manifest_data/<ipfs_hash>")
def get_manifest_data(ipfs_hash: str):
    manifest: ManifestOutput = parse_yml(ipfs_hash)
    return manifest_output_to_json(manifest)



@app.route("/schema_data/<ipfs_hash>")
def get_schema_data(ipfs_hash: str):
    schema: SchemaOutput = parse_gql(ipfs_hash)
    return schema



@app.route("/overview_page/<ipfs_hash>")
def generate_overview(ipfs_hash: str):
    manifest: ManifestOutput = parse_yml(ipfs_hash)
    overview_page: OverviewPage = OverviewPage(manifest)
    overview_page.generate("Testing")
    return {
        "data": overview_page.markdown
    }






@app.route("/docs/<ipfs_hash>")
def make_docs(ipfs_hash: str):
    manifest: ManifestOutput = parse_yml(ipfs_hash)
    schema: SchemaOutput = parse_gql(manifest.schema_hash)
    return f"It's still a work in progress"



