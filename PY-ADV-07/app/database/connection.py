import sys
import os
from pathlib import Path

import psycopg

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.exceptions.database_exceptions import DatabaseConnectionError


def get_connection():
    """Create and return a PostgreSQL database connection."""
    try:
        return psycopg.connect(
            host="localhost",
            port=5432,
            dbname="employee_management",
            user="postgres",
            password=os.getenv("POSTGRES_PASSWORD"),
        )
    except psycopg.Error as exc:
        raise DatabaseConnectionError(
            "Unable to connect to the database."
        ) from exc


if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Database connection successful")
        conn.close()
    except DatabaseConnectionError as exc:
        print(f"Database connection failed: {exc}")