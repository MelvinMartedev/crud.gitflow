from flask import jsonify, request


def register(app, store):
    @app.put("/items/<int:item_id>")
    def update_item(item_id):
        item = store["items"].get(item_id)
        if item is None:
            return jsonify(error="item no encontrado"), 404
        data = request.get_json(silent=True) or {}
        if "name" in data:
            name = (data["name"] or "").strip()
            if not name:
                return jsonify(error="name no puede estar vacio"), 400
            item["name"] = name
        if "description" in data:
            item["description"] = data["description"]
        return jsonify(item)
