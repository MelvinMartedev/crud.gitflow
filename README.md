# CRUD de Items con Flask y Git Flow

API REST sencilla para gestionar items (Create, Read, Update, Delete).

## Ejecutar
    python -m venv .venv
    source .venv/bin/activate    # En Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python app.py

## Endpoints
| Metodo | Ruta          | Descripcion          |
|--------|---------------|----------------------|
| POST   | /items        | Crear un item        |
| GET    | /items        | Listar items         |
| GET    | /items/<id>   | Ver un item          |
| PUT    | /items/<id>   | Actualizar un item   |
| DELETE | /items/<id>   | Eliminar un item     |
| GET    | /health       | Estado del servicio  |

## Tests
    pytest

## Flujo de trabajo
Se usa Git Flow: cada feature nace de `dev` y se integra por Pull Request
a `dev`, luego a `qa` y finalmente a `main`.
