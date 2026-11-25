from app import app, store


def test_delete_item_ok():
    store["items"][300] = {"id": 300, "name": "Borrar", "description": ""}
    res = app.test_client().delete("/items/300")
    assert res.status_code == 204
    assert 300 not in store["items"]


def test_delete_item_inexistente():
    res = app.test_client().delete("/items/99999")
    assert res.status_code == 404
