"""Creates My.App.Person persistent class in IRIS via SQL DDL."""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

ENGINE_URL = (
    f"iris://{os.environ['IRIS_USERNAME']}:{os.environ['IRIS_PASSWORD']}"
    f"@{os.environ['IRIS_HOST']}:{os.environ['IRIS_PORT']}/{os.environ['IRIS_NAMESPACE']}"
)


def setup() -> None:
    engine = create_engine(ENGINE_URL)
    with engine.begin() as conn:
        exists = conn.execute(text(
            "SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES "
            "WHERE TABLE_SCHEMA='My_App' AND TABLE_NAME='Person'"
        )).scalar()

        if exists:
            print("My.App.Person already exists — skipping.")
            return

        conn.execute(text("""
            CREATE TABLE My_App.Person (
                Name  VARCHAR(255),
                DOB   DATE,
                Email VARCHAR(255)
            )
        """))
        print("My.App.Person created.")


if __name__ == "__main__":
    setup()
