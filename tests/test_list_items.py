from app import app, store


def test_list_items():
    store["items"][100] = {"id": 100, "name": "Demo", "description": ""}
    res = app.test_client().get("/items")
    assert res.status_code == 200
    assert any(i["id"] == 100 for i in res.get_json())


def test_get_item_inexistente():
    res = app.test_client().get("/items/99999")
    assert res.status_code == 404
