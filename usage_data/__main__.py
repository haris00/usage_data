import click
import csv
from usage_data.lib import extract_data_from_id, peak_usage, format_peak_usage, expected_savings, \
    format_expected_savings

PEAK_USAGE = 'peak_usage'
EXPECTED_SAVINGS = 'expected_savings'
PERCENTAGE_SAVING = 30
PERIOD = (12, 18)


@click.command()
@click.argument('file_name')
@click.argument('task')
@click.argument('building_id')
def main(file_name, task, building_id):
    """
    Simple CLI for getting energy usage data
    """
    try:
        hours, kwhs_usage = extract_data_from_id(building_id, file_name, csv)
    except FileNotFoundError as e:
        print(f'Cannot find file {file_name}')
        exit()
    if hours is None or kwhs_usage is None:
        print(f'"{building_id}" not in the data set!')
        exit()
    output = "invalid task"
    if task == PEAK_USAGE:
        max_kwh_usage_time, max_kwh_usage = peak_usage(hours, kwhs_usage)
        output = format_peak_usage(max_kwh_usage_time, max_kwh_usage)
    elif task == EXPECTED_SAVINGS:
        kwh_savings = expected_savings(hours, kwhs_usage, PERCENTAGE_SAVING, PERIOD)
        output = format_expected_savings(kwh_savings)

    print(output)


if __name__ == '__main__':
    main()
