from backend import db_helper

def test_fetch_all_records_for_date():
    expenses = db_helper.fetch_all_records_for_date("2024-08-15")
    
    assert len(expenses) == 1
    assert expenses[0]["amount"] == 10
    assert expenses[0]["category"] == "Shopping"
    assert expenses[0]["notes"] == "Bought potatoes"
    
# test for invalid date 
def test_fetch_all_records_for_date_invalid_date():
    expenses = db_helper.fetch_all_records_for_date("9999-08-24")
    
    assert len(expenses) == 0
    
#test for invalid date range 
def test_fetch_expense_summary_invalid_date_range():
    expenses = db_helper.fetch_expense_summary("2024-08-01", "2024-07-01")
    
    assert len(expenses) == 0