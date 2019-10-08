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
@click.argument('id')
def main(file_name, task, id):
    """
    Simple CLI for getting energy usage data
    """
    hours, kwhs_usage = extract_data_from_id(id, file_name, csv)
    output = "invalid"
    if task == PEAK_USAGE:
        max_kwh_usage_time, max_kwh_usage = peak_usage(hours, kwhs_usage)
        output = format_peak_usage(max_kwh_usage_time, max_kwh_usage)
    elif task == EXPECTED_SAVINGS:
        kwh_savings = expected_savings(hours, kwhs_usage, PERCENTAGE_SAVING, PERIOD)
        output = format_expected_savings(kwh_savings)

    print(output)


if __name__ == '__main__':
    main()
