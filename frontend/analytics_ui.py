import pandas as pd
import streamlit as st
from datetime import datetime
from backend import api_handler

def analytics_tab():
    col1, col2 = st.columns(2)
    
    with col1:
        start_date = st.date_input("Start Date", value=datetime(2024, 8, 1))
        
    with col2:
        end_date = st.date_input("End Date", value=datetime(2024, 8, 5))
        
    submit_button = st.button("Get Analytics")
    if submit_button: 
        response = api_handler.get_expense_summary(
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d")
            )
        if response:
            data = {
                "Category": list(response.keys()),
                "Total": [response[category]['total'] for category in response.keys()],
                "Percentage": [response[category]['percentage'] for category in response.keys()]
            }
            
            df = pd.DataFrame(data)
            df_sorted = df.sort_values(by='Percentage', ascending=False)
            
            st.title("Expense Breakdown By Category")
            st.bar_chart(df_sorted.set_index("Category")["Percentage"])
            
            df_sorted["Total"] = df_sorted["Total"].map("${:,.2f}".format)
            df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}%".format)
            
            st.table(df_sorted)
        else:
            st.write("Failed to retrieve analytics")
   
    
