#!/usr/bin/env python

import yaml

from pathlib import Path

def load_template(template_path: Path, name: str) -> str:
    # Mypy knows that `file_path` has a `read_text` method that returns a str
    template = template_path.read_text()
    # ... so it understands this line type checks
    return template.replace('USERNAME', name)

# Function using PyYaml
# stub package: "types-PyYAML" is required for type hint
def load_yaml(path: Path) -> None:
    with open(path, encoding='utf-8') as file:
        obj = yaml.safe_load(file)
    print(obj)
