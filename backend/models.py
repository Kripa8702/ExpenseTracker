from pydantic import BaseModel
from typing import  Optional
from datetime import date

class Expense(BaseModel):
    id: Optional[int] = None
    amount: float
    category: str
    notes: str
    
class DateRange(BaseModel):
    start_date: date
    end_date: date
    
