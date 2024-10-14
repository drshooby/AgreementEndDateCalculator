import unittest
from main.calculator import closest_agreement_date
from datetime import *

class TestCalulator(unittest.TestCase):

    def test_closest_agreement_date(self):

        date_str1 = "2024-10-14"
        date_str2 = "2024-12-31"
        date_str3 = "2025-02-20"

        # Convert the date strings to datetime objects
        date_format = "%Y-%m-%d"  # Define the format (YYYY-MM-DD)
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        date3 = datetime.strptime(date_str3, date_format)

        # test between 3rd and 4th quarter
        r1 = closest_agreement_date("quarter", date1)
        self.assertEqual(r1, "2024-12-31")

        # test input date is a quarter end date
        r2 = closest_agreement_date("quarter", date2)
        self.assertEqual(r2, "2024-12-31")

        # test between 1st and 2nd quarter
        r3 = closest_agreement_date("quarter", date3)
        self.assertEqual(r3, "2025-03-31")