from utils.json_handler import write_json


if __name__ == "__main__":
    new_item = {"name": "CHURROS DO M5", "price": 5.0}
    print(write_json('menu.json', new_item))
