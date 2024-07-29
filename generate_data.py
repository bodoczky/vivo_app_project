import json
import random
from datetime import datetime, timedelta

def generate_data(num_seasons):
    data = {}
    start_year = 1999  #datetime.now().year

    for season in range(num_seasons):
        season_start = start_year + season
        season_end = season_start + 1
        season_key = f"{season_start} - {season_end}"
        data[season_key] = {}

        current_date = datetime(season_start, 9, 1)  # Start from September 1st

        while current_date.year < season_end or (current_date.year == season_end and current_date.month <= 8):
            month_key = current_date.strftime("%B %Y")
            data[season_key][month_key] = {}

            for day in range(1, 29):  # 28 days per month
                day_data = {
                    "Victory": random.randint(3, 6),
                    "Defeat": random.randint(1, 5),
                    "Touches Scored": random.randint(20, 40),
                    "Touches Received": random.randint(20, 30)
                }
                data[season_key][month_key][str(day)] = day_data

            # Move to the next month
            if current_date.month == 12:
                current_date = current_date.replace(year=current_date.year + 1, month=1)
            else:
                current_date = current_date.replace(month=current_date.month + 1)

    return data

def main():
    num_seasons = int(input("Enter the number of seasons to generate: "))
    generated_data = generate_data(num_seasons)

    with open('fencing_data.json', 'w') as f:
        json.dump(generated_data, f, indent=2)

    print(f"Data for {num_seasons} seasons has been generated and saved to 'fencing_data.json'")

if __name__ == "__main__":
    main()