import unittest
from datetime import datetime
from utils import date_utils

class TestDateUtils(unittest.TestCase):

    def test_get_month_year_text(self):
        date = datetime(2023, 7, 15)
        self.assertEqual(date_utils.get_month_year_text(date), "July 2023")

    def test_get_month_year_text_label(self):
        date = datetime(2023, 7, 15)
        self.assertEqual(date_utils.get_month_year_text_label(date), "JULY")

    def test_parse_month_year(self):
        self.assertEqual(date_utils.parse_month_year("July 2023"), datetime(2023, 7, 1))

    def test_get_first_available_date(self):
        dates = ["July 2023", "June 2023", "August 2023"]
        self.assertEqual(date_utils.get_first_available_date(dates), datetime(2023, 6, 1))

    def test_get_last_available_date(self):
        dates = ["July 2023", "June 2023", "August 2023"]
        self.assertEqual(date_utils.get_last_available_date(dates), datetime(2023, 8, 1))

    def test_get_prev_month(self):
        date = datetime(2023, 7, 15)
        self.assertEqual(date_utils.get_prev_month(date), datetime(2023, 6, 1))

    def test_get_next_month(self):
        date = datetime(2023, 7, 15)
        self.assertEqual(date_utils.get_next_month(date), datetime(2023, 8, 1))

    def test_get_day_abbr(self):
        self.assertEqual(date_utils.get_day_abbr("1"), "M") 
        self.assertEqual(date_utils.get_day_abbr("2"), "T")

    def test_get_week_number(self):
        self.assertEqual(date_utils.get_week_number("1"), 1)
        self.assertEqual(date_utils.get_week_number("8"), 2)

    def test_format_date_for_comparison(self):
        date = datetime(2023, 7, 15)
        self.assertEqual(date_utils.format_date_for_comparison(date), "2023-07")

    def test_is_date_in_range(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 12, 31)
        self.assertTrue(date_utils.is_date_in_range("July 2023", start_date, end_date))
        self.assertFalse(date_utils.is_date_in_range("January 2024", start_date, end_date))

    def test_get_months_between(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 3, 1)
        expected = ["January 2023", "February 2023", "March 2023"]
        self.assertEqual(date_utils.get_months_between(start_date, end_date), expected)

if __name__ == '__main__':
    unittest.main()