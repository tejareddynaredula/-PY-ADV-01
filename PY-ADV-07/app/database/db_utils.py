
from app.database.connection import get_connection
from app.exceptions.database_exceptions import DatabaseOperationError


def execute_query(query: str, params=None) -> None:
    """Execute an INSERT, UPDATE, or DELETE query."""
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
        conn.commit()
    except Exception as exc:
        conn.rollback()
        raise DatabaseOperationError(
            "Database operation failed."
        ) from exc
    finally:
        conn.close()


def fetch_all(query: str, params=None) -> list:
    """Execute a SELECT query and return all rows."""
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    except Exception as exc:
        raise DatabaseOperationError(
            "Failed to fetch records."
        ) from exc
    finally:
        conn.close()


def fetch_one(query: str, params=None):
    """Execute a SELECT query and return one row."""
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()
    except Exception as exc:
        raise DatabaseOperationError(
            "Failed to fetch record."
        ) from exc
    finally:
        conn.close()