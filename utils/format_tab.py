def addId(menu: list[dict], tab: dict) -> dict:
    return {
        "id": menu[-1]["id"] + 1 if len(menu) > 0 else len(menu) + 1,
        **tab
        }
