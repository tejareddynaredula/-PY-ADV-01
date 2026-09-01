import psycopg

from app.exceptions.database_exceptions import DatabaseConnectionError


def get_connection():
    """Create and return a PostgreSQL database connection."""
    try:
        return psycopg.connect(
            host="localhost",
            port=5432,
            dbname="employee_management",
            user="postgres",
            password="Naredula97",
        )
    except psycopg.Error as exc:
        raise DatabaseConnectionError(
            "Unable to connect to the database."
        ) from exc