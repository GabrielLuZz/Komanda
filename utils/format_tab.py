def addId(menu: list[dict], tab: dict) -> dict:
    return {
        "id": menu[-1]["id"] + 1 if len(menu) > 0 else 1,
        **tab
        }
