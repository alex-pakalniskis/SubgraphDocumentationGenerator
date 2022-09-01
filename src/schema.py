import requests
from graphql import parse, ObjectTypeDefinitionNode, NamedTypeNode, NonNullTypeNode, ListTypeNode
from classes import SchemaOutput

# doc link: https://github.com/graphql-python/graphql-core/blob/main/docs/usage/parser.rst

# DEBUGGING
def parse_graphql(schema_ipfs_hash: str):
    s = requests.get(f"https://ipfs.io{schema_ipfs_hash}")
    s_text = s.text
    s_graphql = parse(s_text, no_location=True)

    schema = SchemaOutput()
    for obj in s_graphql.definitions:
        if (type(obj) == ObjectTypeDefinitionNode):
            schema.definitions[obj.name.value] = tuple( list(fdn.type.to_dict().values()) for fdn in obj.fields)

            # schema.definitions[obj.name.value] = [tuple({fdn.name.value: fdn.type.to_dict()} for fdn in obj.fields)]
            # schema.definitions[obj.name.value] = [tuple(fdn.type for fdn in obj.fields)]
    schema.definitions.pop('_Schema_', None)


    # for k, v in schema.definitions.items():
    #     if type(v) == NonNullTypeNode:
    #         print(v.name)



    print(schema.definitions["Project"])


    # print(s_graphql)

if __name__ == "__main__":
    schema_hash = "/ipfs/QmV9J3YqyyEasbpJmTqMoQkVi5vvSNuz1RBrMS2cHtJUK2"
    parse_graphql(schema_hash)