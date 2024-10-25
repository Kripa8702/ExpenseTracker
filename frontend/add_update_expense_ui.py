import streamlit as st
from datetime import datetime
from typing import List
from backend import api_handler
from backend.models import Expense

category_options = ['Food', 'Transport', 'Shopping', 'Rent', 'Entertainment', 'Other']

def add_update_expense_tab():
    selected_date = st.date_input("Enter Date", value=datetime(2024, 8,1))
    if selected_date: 
        expenses = api_handler.fetch_expenses_for_date(selected_date)
        if expenses:
            update_expenses_form(expenses)
            
        add_expense_form(selected_date)


def update_expenses_form(expenses: List[Expense]):
    st.subheader("Update Expenses")
    for expense in expenses:
        with st.expander(f"{expense['category']} - {expense['amount']}"):
            st.write(f"Category: {expense['category']}")
            st.write(f"Amount: {expense['amount']}")
            st.write(f"Notes: {expense['notes']}")
            
            st.divider()
            st.caption("Update Expense")
            update_expense_form_item(expense)
        
def update_expense_form_item(expense: Expense):
    
    with st.form(key=f"update_expense_{expense['id']}"):
        amount_col, category_col, notes_col = st.columns([5, 5, 10])
        with amount_col:
            amount_val = st.number_input("Amount", value=expense['amount'], key=f"amount_{expense['id']}", min_value=0.0, step=1.0)
        
        with category_col:
            preselected_category = category_options.index(expense['category'])
            
            category_val = st.selectbox("Category", options=category_options, index= preselected_category, key=f"category_{expense['id']}")
            
        with notes_col:
            notes_val = st.text_input("Notes", value=expense['notes'], key=f"notes_{expense['id']}")
            
        submit_button = st.form_submit_button("Update")
        if submit_button:
            api_handler.update_expense(
                id=expense['id'],
                amount=amount_val,
                category=category_val,
                notes=notes_val
            )
        
def add_expense_form(selected_date: datetime):
    st.subheader("Add Expense")
    with st.form(key='add_expense_form'):
        amount_col, category_col, notes_col = st.columns([5, 5, 10])
        
        with amount_col:
            amount_val = st.number_input("Amount", min_value=0.0, step=1.0)
        
        with category_col:
            category_val = st.selectbox("Category", options=category_options)
            
        with notes_col:
            notes_val = st.text_input("Notes")
            
        submit_button = st.form_submit_button("Add")
        if submit_button:
            api_handler.add_expense(
                expense_date=selected_date,
                amount=amount_val,
                category=category_val,
                notes=notes_val
            )
