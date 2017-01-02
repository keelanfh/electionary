import datetime as dt
import sys

working_directory = 'transcripts-21stDec'

def mean(any_list):
    assert type(any_list) == list or type(any_list) == tuple
    return sum(any_list) / len(any_list)


def list_to_item(any_list):
    for item in any_list:
        return item


def iso_to_datetime(iso_string):
    year = int(iso_string[0:4])
    month = int(iso_string[5:7])
    day = int(iso_string[8:10])
    return dt.date(year, month, day)

if not sys.executable.split('/')[-1] == 'pypy':
    import commonfcpython
