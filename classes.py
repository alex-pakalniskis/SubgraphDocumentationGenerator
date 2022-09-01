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