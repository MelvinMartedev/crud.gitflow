from flask import jsonify, request


def register(app, store):
    @app.post("/items")
    def create_item():
        data = request.get_json(silent=True) or {}
        name = (data.get("name") or "").strip()
        if not name:
            return jsonify(error="name es obligatorio"), 400
        item = {
            "id": store["next_id"],
            "name": name,
            "description": data.get("description", ""),
        }
        store["items"][item["id"]] = item
        store["next_id"] += 1
        return jsonify(item), 201
