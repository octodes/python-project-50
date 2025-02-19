import json
from pathlib import Path

import yaml


def parse(file_path):
    file_extension = Path(file_path).suffix

    match file_extension:
        case ".json":
            return json.load(open(file_path))
        case ".yml" | ".yaml":
            return yaml.safe_load(open(file_path))
        case _:
            raise ValueError(f"Unknown file type: {file_extension[1:]}")

