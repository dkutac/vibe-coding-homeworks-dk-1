import os
from flask import Flask, request, jsonify, abort, render_template
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, text

load_dotenv()

app = Flask(__name__)

ENGINE_URL = (
    f"iris://{os.environ['IRIS_USERNAME']}:{os.environ['IRIS_PASSWORD']}"
    f"@{os.environ['IRIS_HOST']}:{os.environ['IRIS_PORT']}/{os.environ['IRIS_NAMESPACE']}"
)
TABLE = "My_App.Person"


def engine():
    return create_engine(ENGINE_URL)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/persons")
def list_persons():
    df = pd.read_sql(f"SELECT ID, Name, DOB, Email FROM {TABLE}", engine())
    return jsonify(df.to_dict(orient="records"))


@app.get("/persons/<int:person_id>")
def get_person(person_id: int):
    df = pd.read_sql(
        text(f"SELECT ID, Name, DOB, Email FROM {TABLE} WHERE ID = :id"),
        engine(),
        params={"id": person_id},
    )
    if df.empty:
        abort(404)
    return jsonify(df.iloc[0].to_dict())


@app.post("/persons")
def create_person():
    data = request.get_json(force=True)
    with engine().begin() as conn:
        conn.execute(
            text(f"INSERT INTO {TABLE} (Name, DOB, Email) VALUES (:name, :dob, :email)"),
            {"name": data.get("name", ""), "dob": data.get("dob"), "email": data.get("email", "")},
        )
        new_id = conn.execute(text(f"SELECT MAX(ID) FROM {TABLE}")).scalar()

    return get_person(new_id), 201


@app.put("/persons/<int:person_id>")
def update_person(person_id: int):
    data = request.get_json(force=True)
    allowed = {"name": "Name", "dob": "DOB", "email": "Email"}
    updates = {col: data[key] for key, col in allowed.items() if key in data}
    if not updates:
        abort(400, description="No valid fields provided.")

    set_clause = ", ".join(f"{col} = :{col}" for col in updates)
    updates["id"] = person_id

    with engine().begin() as conn:
        rows = conn.execute(
            text(f"UPDATE {TABLE} SET {set_clause} WHERE ID = :id"),
            updates,
        ).rowcount

    if rows == 0:
        abort(404)
    return get_person(person_id)


@app.delete("/persons/<int:person_id>")
def delete_person(person_id: int):
    with engine().begin() as conn:
        rows = conn.execute(
            text(f"DELETE FROM {TABLE} WHERE ID = :id"),
            {"id": person_id},
        ).rowcount
    if rows == 0:
        abort(404)
    return "", 204
