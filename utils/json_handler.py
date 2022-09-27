from ast import FormattedValue
import json
from json.decoder import JSONDecodeError
from .format_tab import addId

FILEPATH = 'menu.json'


def read_json(filepath: str) -> list[dict]:
    try:
        with open(filepath, encoding='windows-1252') as file:
            return json.load(file)
    except (JSONDecodeError, FileNotFoundError):
        return []


def write_json(filepath: str, payload: dict) -> dict:
    data = read_json(filepath)
    FormattedPayload = addId(data, payload)
    data.append(FormattedPayload)

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False, )
        return FormattedPayload
