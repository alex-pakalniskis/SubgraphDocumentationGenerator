import requests
import yaml
import re
from classes import DataSource, ManifestOutput, SchemaOutput, OverviewPage, EntitiesPage, QueriesPage


def parse_yml(manifest_ipfs_hash: str) -> ManifestOutput:
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
    
    return ManifestOutput(
        description=description, 
        repository=repository, 
        spec_version=spec_version, 
        schema_hash=schema_hash, 
        data_sources=data_sources
        )


def manifest_data_sources_to_json(manifest: ManifestOutput) -> dict():
    data = dict()
    for i in range(len(manifest.data_sources)):
        data[i] = {}
        data[i]["kind"] = manifest.data_sources[i].kind
        data[i]["mapping"] = manifest.data_sources[i].mapping
        data[i]["name"] = manifest.data_sources[i].name
        data[i]["network"] = manifest.data_sources[i].network
        data[i]["source"] = manifest.data_sources[i].source
        return data

def manifest_output_to_json(manifest) -> dict:
    data = dict()
    data["schema_hash"] = manifest.schema_hash
    data["repository"] = manifest.repository
    data["spec_version"] = manifest.spec_version
    data["description"] = manifest.description
    data["data_sources"] = manifest_data_sources_to_json(manifest)
    return data




def parse_gql(schema_ipfs_hash: str, commented:bool = True):
    if commented == True:
        s = requests.get(f"https://ipfs.io{schema_ipfs_hash}")
        s_text = s.text
        schema = SchemaOutput(schema_ipfs_hash)

        s_text_split = s_text.split('\n}\n')
        for elem in s_text_split:
            schema.entities_data.append(elem)
        
        for entity in schema.entities_data:
            if "type" in entity:
                splitted = entity.split("\ntype ")
                name = splitted[1].split(" ")[0]
                schema.entities[name] = dict()
                if len(splitted[0]) > 0:
                    schema.entities[name]["entity_comment"] = splitted[0].replace('"""','').replace("\n","")
        
                
                if "@entity" in splitted[1]:
                    fields_data = splitted[1].split("@entity {\n")[1]

                    fields_data_no_desc = re.sub('".*?"', '', fields_data)
                    fields_data_no_desc = re.sub('#.*?\n', '', fields_data)

                    # fields_comment_and_name = fields_data_no_desc.split(": ")[0]
                    # fields_comment = fields_comment_and_name.split("\n")[0]
                    # schema.entities[name]["field_comment_and_name"] = fields_comment_and_name

                    schema.entities[name]["fields"] = fields_data_no_desc
                    # TODO
        
        # print(schema.entities["Project"])

    else:
        print("Taking a different parsing strategy")
        print("The devs still need to add this functionality")
        print("Please check back soon or open a GitHub issue")


def generate_overview_page(manifest_data: ManifestOutput):
    overview_page = OverviewPage(manifest_data)
    # Update to remove hard-coded subgraph name
    overview_page.generate("Everest")
    overview_page.save()

def generate_entities_page(schema_data: SchemaOutput):
    entities_page = EntitiesPage(schema_data)
    entities_page.generate()
    entities_page.save()

def generate_queries_page(schema_data: SchemaOutput):
    entities_page = QueriesPage(schema_data)
    entities_page.generate()
    entities_page.save()

