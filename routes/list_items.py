from flask import jsonify


def register(app, store):
    @app.get("/items")
    def list_items():
        return jsonify(list(store["items"].values()))

    @app.get("/items/<int:item_id>")
    def get_item(item_id):
        item = store["items"].get(item_id)
        if item is None:
            return jsonify(error="item no encontrado"), 404
        return jsonify(item)
