from app import app


def test_create_item_ok():
    res = app.test_client().post("/items", json={"name": "Lapiz"})
    assert res.status_code == 201
    assert res.get_json()["name"] == "Lapiz"


def test_create_item_sin_nombre():
    res = app.test_client().post("/items", json={})
    assert res.status_code == 400
