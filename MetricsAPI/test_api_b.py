import unittest
from app import get_average_monthly_value_metrics_a

class TestAPIB(unittest.TestCase):

    def test_calculate_daily_national_estimate_metrics_b(self):
        result = get_average_monthly_value_metrics_a("col","2022-06-01","2023-07-01")        

        self.assertEqual(result, None)
