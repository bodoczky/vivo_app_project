import json
from datetime import datetime

class DataManager:
    def __init__(self, data_file='fencing_data.json'):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def get_seasons(self):
        return list(self.data.keys())

    def get_month_data(self, season, month_year):
        return self.data.get(season, {}).get(month_year, {})

    def calculate_weekly_totals(self, season, month_year):
        month_data = self.get_month_data(season, month_year)
        weekly_totals = {}
        
        for day, day_data in month_data.items():
            day_num = int(day)
            week_num = (day_num - 1) // 7 + 1
            
            if week_num not in weekly_totals:
                weekly_totals[week_num] = {
                    'Victory': 0,
                    'Defeat': 0,
                    'Touches Scored': 0,
                    'Touches Received': 0
                }
            
            for category in ['Victory', 'Defeat', 'Touches Scored', 'Touches Received']:
                weekly_totals[week_num][category] += day_data[category]
        
        return weekly_totals

    def get_available_months(self, season):
        return list(self.data.get(season, {}).keys())