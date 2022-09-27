def addId(menu: list[dict], tab: dict) -> dict:
    print(menu)
    print(tab)
    return {
        "id": menu[-1]["id"] + 1 if len(menu) > 0 else 1,
        **tab
        }
