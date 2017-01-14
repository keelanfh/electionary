from __future__ import division
import datetime as dt
import sys
import os

import unicodedata

working_directory = 'transcripts-12thJan'


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


def generate_rawgit_url(filepath):
    return "https://rawgit.com/keelanfh/electionary/master/" + filepath


def generate_rawgit_img_embed(filepath):
    return "<img src=\"" + generate_rawgit_url(filepath) + "\"/>"


def is_pypy():
    if sys.executable.split('/')[-1] == 'pypy':
        return True
    else:
        return False


if not is_pypy():
    from commonfcpython import *
else:
    class TranscriptSelector(object):
        def __init__(self, text):
            raise Exception('Switch to CPython interpreter to instantiate TranscriptSelector')


