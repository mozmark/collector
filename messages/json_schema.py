from jsonschema import validate

# TODO: make a custom validator to discard extra attributes

''' a validator to validate documents against a json schema '''
class SchemaValidator:
    def __init__(self, schema):
        print 'SchemaValidator init'
        print schema
        self.schema = schema

    def validate(self, json):
        print 'SchemaValidator validate'
        return validate(json, self.schema)
