import unittest
import csv
from usage_data.lib import extract_data_from_id, peak_usage, format_peak_usage, expected_savings, \
    format_expected_savings


class UsageData(unittest.TestCase):

    def test_extract_data_from_id(self):
        hours = list(range(0, 23))
        kwhs_usage = [4.898962, 4.725122, 5.889937, 7.055993, 8.147902, 9.526529, 9.654547, 9.497643, 7.656154, 6.922413
                      , 4.821351, 5.117135, 6.103418, 7.221611, 10.372388, 12.87602, 15.43456, 18.041841, 18.20572,
                      16.7765, 15.114921, 12.12373, 8.830045]
        extracted_hours, extracted_kwhs_usage = extract_data_from_id('white_house', 'test_data/example_homes_data', csv)
        self.assertEqual((extracted_hours, extracted_kwhs_usage), (hours, kwhs_usage))

    def test_peak_usage(self):
        hours = list(range(0, 23))
        kwhs_usage = [4.898962, 4.725122, 5.889937, 7.055993, 8.147902, 9.526529, 9.654547, 9.497643, 7.656154, 6.922413
                      , 4.821351, 5.117135, 6.103418, 7.221611, 10.372388, 12.87602, 15.43456, 18.041841, 18.20572,
                      16.7765, 15.114921, 12.12373, 8.830045]
        self.assertEqual(peak_usage(hours, kwhs_usage), (19, 18.20572))

    def test_format_peak_usage(self):
        time = 75.7829
        kwh_usage = 13
        self.assertEqual(format_peak_usage(time, kwh_usage), "74.5 kWh at 13:00")

    def test_expected_savings(self):
        hours = list(range(0, 23))
        kwhs_usage = [4.898962, 4.725122, 5.889937, 7.055993, 8.147902, 9.526529, 9.654547, 9.497643, 7.656154, 6.922413
                      , 4.821351, 5.117135, 6.103418, 7.221611, 10.372388, 12.87602, 15.43456, 18.041841, 18.20572,
                      16.7765, 15.114921, 12.12373, 8.830045]

        self.assertEqual(expected_savings(hours, kwhs_usage, 30, (12, 18)), 22.550091899999998)

    def test_format_expected_savings(self):
        kwh_savings = 30.37
        self.assertEqual(format_expected_savings(kwh_savings), "30 kWh")


if __name__ == '__main__':
    unittest.main()
