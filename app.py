import importlib
import pkgutil

from flask import Flask

import routes

# Almacenamiento en memoria para el CRUD de items
store = {"items": {}, "next_id": 1}


def create_app():
    app = Flask(__name__)
    # Carga automaticamente cada modulo de routes/ (cada uno es una feature)
    for mod in pkgutil.iter_modules(routes.__path__):
        importlib.import_module(f"routes.{mod.name}").register(app, store)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
