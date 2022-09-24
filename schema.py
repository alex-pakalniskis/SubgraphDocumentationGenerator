import requests
import re
from classes import SchemaOutput


def parse_graphql(schema_ipfs_hash: str, commented:bool = True):
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
        
        print(schema.entities["Project"])

            

    else:
        print("Taking a different parsing strategy")



def main():
    schema_hash = "/ipfs/QmV9J3YqyyEasbpJmTqMoQkVi5vvSNuz1RBrMS2cHtJUK2"
    parse_graphql(schema_hash)


if __name__ == "__main__":
    main()