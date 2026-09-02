import os
import psycopg


def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="employee_management",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD")
    )
