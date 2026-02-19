import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        port = 3306,
        password="root",  # Change this if needed
        database="expense_manager"
    )
    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()


def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        return cursor.fetchall()


def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def insert_expense(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def fetch_expense_summary(start_date, end_date):
    with get_db_cursor() as cursor:
        cursor.execute(
            """SELECT category, SUM(amount) as total 
               FROM expenses 
               WHERE expense_date BETWEEN %s AND %s 
               GROUP BY category""",
            (start_date, end_date)
        )
        return cursor.fetchall()
