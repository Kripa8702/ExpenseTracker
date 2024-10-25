# add project root
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(f"Adding {project_root} to sys.path")
sys.path.insert(0, project_root)


import streamlit as st
from add_update_expense_ui import add_update_expense_tab
from analytics_ui import analytics_tab

st.title('Expense Tracker')

tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
        add_update_expense_tab()
        
with tab2:
        analytics_tab()
    
