from typing import List

class DataSource:
    def __init__(self, kind: str, mapping: dict, name: str, network: str, source: dict):
        self.kind = kind
        self.mapping = mapping
        self.name = name
        self.network = network
        self.source = source

class ManifestOutput:
    def __init__(self, description: str, repository: str, spec_version: str, schema_hash: str, data_sources: List[DataSource]):
        self.description = description
        self.repository = repository
        self.spec_version = spec_version
        self.schema_hash = schema_hash
        self.data_sources = data_sources

class SchemaOutput:
    def __init__(self, definitions: dict = dict() ):
        self.definitions = definitions



class OverviewPage:
    def __init__(self, manifest: ManifestOutput):
        self.description = manifest.description
        self.repository = manifest.repository
        self.spec_version = manifest.spec_version
        self.data_sources = manifest.data_sources
        self.markdown = ""

    def generate(self, project_name: str):
        self.markdown += f"# Subgraph Overview\n"
        self.markdown += f"{project_name} has a GraphQL API endpoint hosted by [The Graph](https://thegraph.com/docs/about/introduction#what-the-graph-is) called a subgraph for indexing and organizing data from the Everest smart contracts. The code for our subgraph(s) can be found [here]({self.repository}).\n\n"
        self.markdown += f"## Official subgraphs\n"
        self.markdown += f"Official subgraphs are subgraphs maintained by the {project_name} team.\n\n"
        

    def save(self):
        with open("../overview.md", "w") as f:
            f.write(self.markdown)