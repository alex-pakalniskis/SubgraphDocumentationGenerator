import requests
import yaml
from classes import DataSource, ManifestOutput

def parse(manifest_ipfs_hash: str) -> ManifestOutput:
    m = requests.get(f"https://ipfs.io/ipfs/{manifest_ipfs_hash}")
    manifest_yml = yaml.safe_load(m.text)

    data_sources = []
    for source in manifest_yml["dataSources"]:
        ds = DataSource(
            kind=source["kind"], 
            mapping=source["mapping"], 
            name=source["name"], 
            network=source["network"], 
            source=source["source"]
            )

        data_sources.append(ds)
    
    description = manifest_yml["description"]
    repository = manifest_yml["repository"]
    spec_version = manifest_yml["specVersion"]
    schema_hash = list(manifest_yml["schema"]["file"].values())[0]    
    
    return ManifestOutput(description=description, repository=repository, spec_version=spec_version, schema_hash=schema_hash, data_sources=data_sources)


def main():
    manifest_hash: str = "QmVsp1bC9rS3rf861cXgyvsqkpdsTXKSnS4729boXZvZyH"
    manifest = parse(manifest_hash)
    for source in manifest.data_sources:
        print(source.kind)
        print(source.mapping)
        print(source.name)
        print(source.network)
        print(source.source)
        print("\n")

if __name__ == "__main__":
    main()