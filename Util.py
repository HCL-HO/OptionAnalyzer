import json


def print_class(o):
    print(json.dumps(o, indent=4, sort_keys=True, default=lambda x: x.__dict__))
