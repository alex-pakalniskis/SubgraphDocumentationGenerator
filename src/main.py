from manifest import parse
from schema import parse_graphql

def main():
    manifest_hash: str = "QmVsp1bC9rS3rf861cXgyvsqkpdsTXKSnS4729boXZvZyH"
    manifest_data = parse(manifest_hash)
    schema = parse_graphql(manifest_data.schema_hash)

if __name__ == "__main__":
    main()