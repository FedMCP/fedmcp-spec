import json,sys, pathlib, jsonschema
SCHEMA=json.load(open(pathlib.Path(__file__).parent/'spec'/'mcp-fed.schema.json'))
jsonschema.validate(json.load(open(sys.argv[1])), SCHEMA)
print("✅", sys.argv[1], "valid")
