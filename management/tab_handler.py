from re import sub
from utils.json_handler import read_json, FILEPATH
from datetime import datetime as dt


def calculate_tab(consumptions: list[dict]) -> dict:
    subtotal = 0

    menu = read_json(FILEPATH)

    for order in consumptions:
        for plate in menu:
            if order['id'] == plate['id']:
                subtotal += plate['price'] * order['amount']
    return {
        'subtotal': subtotal,
        'created_at': dt.now().strftime('%d/%m/%Y %H:%M:%S')
    }
