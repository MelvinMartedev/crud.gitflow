from flask import jsonify


def register(app, store):
    @app.get("/health")
    def health():
        return jsonify(status="ok", total_items=len(store["items"]))
