def extract_data_from_id(id, file_name, csv):
    with open(file_name) as usage_data:
        csv_reader = csv.reader(usage_data, delimiter=',')
        # to skip the header
        next(csv_reader)
        hours = []
        kwhs_usage = []
        for row in csv_reader:
            if str(row[0]) == str(id):
                hours.append(int(row[1]))
                kwhs_usage.append(float(row[2]))
    hours_kwh_usage_bundle = list(zip(hours, kwhs_usage))
    hours_kwh_usage_bundle.sort(key=lambda x: x[0])
    hours, kwhs_usage = zip(*hours_kwh_usage_bundle)
    return tuple(hours), tuple(kwhs_usage)


def peak_usage(hours, kwhs_usage):
    """Returns peak kwh usage and associated hour
    Note: hours and kwhs are assumed sorted
    """
    max_kwh_usage = max(kwhs_usage)
    # Note if there are multiple same values, the one with the lower index is used
    max_index = kwhs_usage.index(max_kwh_usage)
    max_kwh_usage_time = hours[max_index]
    return max_kwh_usage_time, max_kwh_usage


def format_peak_usage(time, kwh_usage):
    formatted_time = f"{str(time).rjust(1, '0')}:00"
    formatted_kwh = round(kwh_usage, 1)
    output_format = f'{formatted_kwh} kWh at {formatted_time}'
    return output_format


def expected_savings(hours, kwhs_usage, percentage_saving, period):
    """Returns expected savings in kwh and associated hour
    Note: hours and kwhs are assumed sorted
    """
    saving_starting_index = hours.index(period[0])
    saving_ending_index = hours.index(period[1])
    kwh_usage_in_period = sum(kwhs_usage[saving_starting_index: saving_ending_index + 1])
    savings = kwh_usage_in_period * (percentage_saving) / 100
    return savings


def format_expected_savings(kwh_savings):
    formatted_kwh_savings = round(kwh_savings, 1)
    output_format = f'{formatted_kwh_savings} kWh'
    return output_format

