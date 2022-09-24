from classes import EntitiesPage, ManifestOutput, OverviewPage, QueriesPage, SchemaOutput
from manifest import parse

def main():
    # Download and parse data
    manifest_hash: str = "QmVsp1bC9rS3rf861cXgyvsqkpdsTXKSnS4729boXZvZyH"
    manifest_data: ManifestOutput = parse(manifest_hash)

    schema_hash: str = "QmV9J3YqyyEasbpJmTqMoQkVi5vvSNuz1RBrMS2cHtJUK2"
    schema_data = SchemaOutput(schema_hash)
    
    # Generate markdown files
    overview_page = OverviewPage(manifest_data)
    overview_page.generate("Everest")
    overview_page.save()

    entities_page = EntitiesPage(schema_data)
    entities_page.generate()
    entities_page.save()

    queries_page = QueriesPage(schema_data)
    queries_page.generate()
    queries_page.save()


if __name__ == "__main__":
    main()