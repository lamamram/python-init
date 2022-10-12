from datetime import datetime

def to_lower(s: str):
    return s.lower()

def today_at(h, m):
    today = datetime.now()
    return datetime(
        today.year, 
        today.month, 
        today.day,
        h,
        m
    )