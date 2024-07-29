from datetime import datetime, timedelta
from calendar import day_abbr

def get_month_year_text(date):
    return date.strftime("%B %Y")

def get_month_year_text_label(date):
    return date.strftime("%B").upper()

def parse_month_year(month_year_string):
    return datetime.strptime(month_year_string, "%B %Y")

def get_first_available_date(dates):
    return min(parse_month_year(date) for date in dates)

def get_last_available_date(dates):
    return max(parse_month_year(date) for date in dates)

def get_prev_month(current_date):
    return (current_date.replace(day=1) - timedelta(days=1)).replace(day=1)

def get_next_month(current_date):
    return (current_date.replace(day=28) + timedelta(days=4)).replace(day=1)

def get_day_abbr(day):
    return day_abbr[datetime(2024, 1, int(day)).weekday()][:1]

def get_week_number(day):
    return (int(day) - 1) // 7 + 1

def format_date_for_comparison(date):
    return date.strftime("%Y-%m")

def is_date_in_range(date, start_date, end_date):
    date = parse_month_year(date)
    return start_date <= date <= end_date

def get_months_between(start_date, end_date):
    months = []
    current_date = start_date
    while current_date <= end_date:
        months.append(get_month_year_text(current_date))
        current_date = get_next_month(current_date)
    return months