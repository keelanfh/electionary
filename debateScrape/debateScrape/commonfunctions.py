from __future__ import division
import datetime as dt
import sys

import unicodedata

working_directory = 'transcripts-3rdJan'


def campaign_year_from_year(year):
    if not year % 4:
        return year
    else:
        return year - year % 4 + 4


def mean(any_list):
    assert type(any_list) == list or type(any_list) == tuple
    assert not [True for x in any_list if not (type(x) == float or type(x) == int)]
    result = sum(any_list) / len(any_list)
    return int(result) if int(result) == result else result


def list_to_item(any_list):
    for item in any_list:
        return item


def iso_to_datetime(iso_string):
    year = int(iso_string[0:4])
    month = int(iso_string[5:7])
    day = int(iso_string[8:10])
    return dt.date(year, month, day)


def unicode_to_ascii(unicode_object):
    return unicodedata.normalize('NFKD', unicode_object).encode(
        'ascii', 'ignore')


if not sys.executable.split('/')[-1] == 'pypy':
    from commonfcpython import *
else:
    class TranscriptSelector(object):
        def __init__(self, text):
            raise Exception('Switch to CPython interpreter to instantiate TranscriptSelector')
