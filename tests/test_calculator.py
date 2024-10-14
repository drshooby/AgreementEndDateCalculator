import unittest
from main.calculator import closest_agreement_end_date, generate_date_ranges
from datetime import *

class TestCalulator(unittest.TestCase):

    def test_closest_agreement_end_date(self):

        date_str1 = "2024-10-14"
        date_str2 = "2024-12-31"
        date_str3 = "2025-02-20"

        # Convert the date strings to datetime objects
        date_format = "%Y-%m-%d"  # Define the format (YYYY-MM-DD)
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        date3 = datetime.strptime(date_str3, date_format)

        # test between 3rd and 4th quarter
        r1 = closest_agreement_end_date("quarter", date1)
        self.assertEqual(r1, datetime(2024, 12, 31, 0, 0))

        # test input date is a quarter end date
        r2 = closest_agreement_end_date("quarter", date2)
        self.assertEqual(r2, datetime(2024, 12, 31, 0, 0))

        # test between 1st and 2nd quarter
        r3 = closest_agreement_end_date("quarter", date3)
        self.assertEqual(r3, datetime(2025, 3, 31, 0, 0))

    def test_generate_date_ranges(self):

        date_str1 = "2024-06-15"
        
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date_str1, date_format)

        req_date = 20
        ONE_YEAR = 365

        single_range, all_ranges = generate_date_ranges("quarter", date1, ONE_YEAR, req_date)

        self.assertEqual(single_range, [(datetime(2024, 6, 30, 0, 0), datetime(2024, 7, 20, 0, 0))])
        self.assertEqual(all_ranges,
            [   (datetime(2024, 6, 30, 0, 0), datetime(2024, 7, 20, 0, 0)),
                (datetime(2024, 9, 30, 0, 0), datetime(2024, 10, 20, 0, 0)),
                (datetime(2024, 12, 31, 0, 0), datetime(2025, 1, 20, 0, 0)),
                (datetime(2025, 3, 31, 0, 0), datetime(2025, 4, 20, 0, 0))    ]
        )