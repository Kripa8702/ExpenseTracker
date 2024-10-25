import mysql.connector
from contextlib import contextmanager
from models import Expense
from typing import List
from logging_setup import setup_logging

logger = setup_logging("db_helper")

@contextmanager
def get_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager",
    )   
        
    cursor = connection.cursor(dictionary=True)
    
    yield cursor
    
    if commit: 
        connection.commit()
    
    cursor.close()
    connection.close()


def fetch_all_records():
    logger.info(f"fetch_all_records called")
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
            
        return expenses
    
    
def fetch_all_records_for_date(expense_date):
    logger.info(f"fetch_all_records_for_date called with date {expense_date}")
    with get_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
        
        return expenses
    
def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start_date {start_date} and end_date {end_date}")
    with get_cursor() as cursor:
        cursor.execute('''SELECT category, sum(amount) as total 
                       FROM expenses WHERE expense_date 
                       BETWEEN %s AND %s 
                       GROUP BY category''', (start_date, end_date))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)
        
        return expenses
            
            
def insert_records(expense_date, expenses: List[Expense]):
    logger.info(f"insert_records called with date {expense_date}")
    with get_cursor(commit=True) as cursor:
        for expense in expenses:
            cursor.execute("INSERT INTO expenses(expense_date, amount, category, notes) VALUES(%s, %s, %s, %s)",
                           (expense_date, expense.amount, expense.category, expense.notes))

def insert_record(expense_date, amount, category, notes):
    logger.info(f"insert_record called with date {expense_date}")
    with get_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses(expense_date, amount, category, notes) VALUES(%s, %s, %s, %s)",
                       (expense_date, amount, category, notes))
        
def update_expense(expense_id, amount, category, notes):
    logger.info(f"update_expense called with id {expense_id}")
    with get_cursor(commit=True) as cursor:
        cursor.execute("UPDATE expenses SET amount = %s, category = %s, notes = %s WHERE id = %s",
                       (amount, category, notes, expense_id))
        
def delete_expense_for_date(expense_date):
    logger.info(f"delete_expense_for_date called with date {expense_date}")
    with get_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))
        

    
if __name__ == "__main__":
    fetch_expense_summary("2024-08-01", "2024-08-05")