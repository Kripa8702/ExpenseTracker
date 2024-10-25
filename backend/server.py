from fastapi import FastAPI
from datetime import date
from typing import List
from models import Expense
from models import DateRange
from fastapi import HTTPException

import db_helper

app = FastAPI()

@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_all_records_for_date(expense_date)
    return expenses

@app.post("/expenses/{expense_date}")
def insert_expenses(expense_date: date, expenses: List[Expense]):
    db_helper.insert_records(expense_date, expenses)
    return {"message": "Expenses added successfully"}

@app.put("/expense")
def update_expense(expense: Expense):
    db_helper.update_expense(expense.id, expense.amount, expense.category, expense.notes)
    return {"message": "Expense updated successfully"}

@app.post("/analytics")
def get_expense_summary(date_range: DateRange):
    expenses = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if expenses is None:
        raise HTTPException(status_code=404, detail="Failed to retrieve expense summary")
    
    break_down = {}
    total = sum([expense['total'] for expense in expenses])
    
    for expense in expenses: 
        percentage = (expense['total'] / total) * 100
        break_down[expense['category']] = {
            "total": expense['total']. __round__(2),    
            "percentage": percentage.__round__(2)
        }
        
    return break_down

