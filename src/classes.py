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
    def __init__(self, ipfs_hash: str):
        self.ipfs_hash = ipfs_hash
        self.entities_data = []
        self.entities: dict = dict()

class OverviewPage:
    def __init__(self, manifest: ManifestOutput):
        self.description = manifest.description
        self.repository = manifest.repository
        self.spec_version = manifest.spec_version
        self.data_sources = manifest.data_sources
        self.markdown = ""

    def generate(self, project_name: str) -> str:
        self.markdown += f"# Subgraph Overview\n"
        self.markdown += f"{project_name} has a GraphQL API endpoint hosted by [The Graph](https://thegraph.com/docs/about/introduction#what-the-graph-is) called a subgraph for indexing and organizing data from the Everest smart contracts. The code for our subgraph(s) can be found [here]({self.repository}).\n\n"
        self.markdown += f"## Official subgraphs\n"
        self.markdown += f"Official subgraphs are subgraphs maintained by the {project_name} team.\n\n"
        self.markdown += f"| Smart Contract | Address | \n"
        self.markdown += f"| --- | --- | \n"

        for source in self.data_sources:
            self.markdown += f"| {source.name} | {source.source['address']} | \n"

        self.markdown += f"\n"
        self.markdown += f"An [API key](https://thegraph.com/docs/en/querying/managing-api-keys/) needed is needed to query our Ethereum subgraph, as it's based on [The Graph](https://thegraph.com/)'s decentralized network. Replace [api-key] with your API key in the API endpoint. [Here](https://thegraph.com/docs/en/studio/managing-api-keys/) is a good guide on how to manage your API keys and set indexer preferences.\n"
        self.markdown += f"* [Creating an API Key Video Tutorial](https://www.youtube.com/watch?v=UrfIpm-Vlgs)\n"        

    def save(self):
        with open("../overview.md", "w") as f:
            f.write(self.markdown)
    


class EntitiesPage:
    def __init__(self, schema: SchemaOutput):
        self.schema = schema
        self.markdown = ""
    
    def generate(self) -> str:
        self.markdown += f"# Subgraph Entities\n"
        
        self.markdown += f"* Bulletted list of entities will go here"
        self.markdown += f"\n"

        self.markdown += f"ELEMENT PLACEHOLDER\n"
        self.markdown += f"| Field | Type | Description | \n"
        self.markdown += f"| --- | --- | --- | \n"
    
    def save(self):
        with open("../entities.md", "w") as f:
            f.write(self.markdown)



class QueriesPage:
    def __init__(self, schema: SchemaOutput):
        self.schema = schema
        self.markdown = ""
    
    def generate(self) -> str:
        self.markdown += f"# Sample Queries\n"
        self.markdown += f"Below are some sample queries you can use to gather information from the smart contracts."
        self.markdown += f"You can build your own queries using a [GraphQL Explorer](https://graphiql-online.com/graphiql) and enter your endpoint to limit the data to exactly what you need.\n"
        self.markdown += f"## Placeholder secondary title \n"
        self.markdown += f"Description: PLACEHOLDER TEXT\n"
        self.markdown += f"``` graphql\n query ... \n```"

    
    def save(self):
        with open("../queries.md", "w") as f:
            f.write(self.markdown)