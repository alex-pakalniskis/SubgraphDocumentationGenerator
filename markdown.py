from classes import ManifestOutput, OverviewPage
from manifest import parse

if __name__ == "__main__":
    manifest_hash: str = "QmVsp1bC9rS3rf861cXgyvsqkpdsTXKSnS4729boXZvZyH"
    manifest_data: ManifestOutput = parse(manifest_hash)

    overview_page = OverviewPage(manifest_data)
    overview_page.generate("Everest")
    overview_page.save()



    # TODO
    # Schema Entities
    # Sample Queries