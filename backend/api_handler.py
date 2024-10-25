import requests

API_URL = 'http://127.0.0.1:8000'

def fetch_expenses_for_date(expense_date):
    try:
        response = requests.get(f'{API_URL}/expenses/{expense_date}')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching expenses for date {expense_date}: {e}")
        return None
    
def update_expense(id, amount, category, notes):
    try:
        response = requests.put(f'{API_URL}/expense', 
                                json={
                                    "id": id,
                                    "amount": amount,
                                    "category": category, 
                                    "notes": notes,
                                        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error updating expense with id {id}: {e}")
        return None
    
def add_expense(expense_date, amount, category, notes):
    try:
        response = requests.post(f'{API_URL}/expenses/{expense_date}', 
                                 json=[{
                                     "amount": amount,
                                     "category": category,
                                     "notes": notes
                                 }])
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error adding expense: {e}")
        return None
    
def get_expense_summary(start_date, end_date):
    try:
        response = requests.post(f'{API_URL}/analytics', 
                                json={
                                    "start_date": start_date,
                                    "end_date": end_date
                                })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching expense summary: {e}")
        return None