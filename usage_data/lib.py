def extract_data_from_id(id, file_name, csv):
    return (None, None)


def peak_usage(hours, kwhs_usage):
    """Returns peak kwh usage and associated hour"""
    max_kwh_usage = max(kwhs_usage)
    max_index = kwhs_usage.index(max_kwh_usage)
    max_kwh_usage_time = hours[max_index]
    return max_kwh_usage_time, max_kwh_usage


def format_peak_usage(time, kwh_usage):
    pass


def expected_savings(hours, kwhs_usage, percentage_saving, period):
    pass


def format_expected_savings(kwh_savings):
    pass

