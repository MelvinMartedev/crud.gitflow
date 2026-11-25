from app import app, store


def test_update_item_ok():
    store["items"][200] = {"id": 200, "name": "Viejo", "description": ""}
    res = app.test_client().put("/items/200", json={"name": "Nuevo"})
    assert res.status_code == 200
    assert res.get_json()["name"] == "Nuevo"


def test_update_item_inexistente():
    res = app.test_client().put("/items/99999", json={"name": "X"})
    assert res.status_code == 404
