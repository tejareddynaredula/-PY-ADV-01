import sys
import pandas as pd

sys.path.insert(0, "PY-ADV-10")

from database.db import get_connection


def read_employee_data():
    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM employees",
        conn
    )

    conn.close()
    return df


def generate_statistics(df):
    print("\nEmployee Statistics:")
    print("Total Employees:", len(df))
    print("Average Age:", df["age"].mean())
    print("Average Salary:", df["salary"].mean())
    print("Highest Salary:", df["salary"].max())
    print("Lowest Salary:", df["salary"].min())


if __name__ == "__main__":
    df = read_employee_data()

    print("Employee Data:")
    print(df)

    generate_statistics(df)