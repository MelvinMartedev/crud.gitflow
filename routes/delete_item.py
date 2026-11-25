from flask import jsonify


def register(app, store):
    @app.delete("/items/<int:item_id>")
    def delete_item(item_id):
        if item_id not in store["items"]:
            return jsonify(error="item no encontrado"), 404
        del store["items"][item_id]
        return "", 204
