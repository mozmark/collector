import os.path
import json
from json_schema import SchemaValidator

dir = os.path.dirname(__file__)

def is_valid(json, validators):
    print 'is_valid'
    for validator in validators:
        try:
            print 'validating with:'
            print validator
            validator.validate(json)
            return True
        except Exception as e:
            # TODO: we may want to log these if we're in debug mode
            pass
    return False

def v1():
    schema_file = os.path.join(dir,"schema","hpkp-report.json")
    return [SchemaValidator(json.load(open(schema_file)))]
