# Data Usage

A simple CLI application that extracts peak energy usage and expected savings from a csv file.
## Getting Started

### Requirements

* Python 3.7.2
* pip

Also you would need a data file in csv format to parse
### Installing

To perform an editable install within a virtual environment:

```
python -m venv env
source env/bin/activate
git clone https://github.com/haris00/usage_data
pip install usage_data
```

## Running the tests

```
cd usage_data
pip install -r test_requirements
nosetests tests
```

## Usage

```
usage_data FILE_NAME TASK BUILDING_ID
```

For example:
```
usage_data example_homes_data.csv expected_savings white_museum
```

The options for TASKS are:
* peak_usage
* expected_savings