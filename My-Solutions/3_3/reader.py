import csv
import collections
import collections.abc

def read_csv_as_dicts(filename='../../Data/portfolio.csv', coltypes=list):
    '''
    Read the bus ride data as a list of dicts
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = []
        for row in rows:
            record = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    path = '../../Data/' + filename
    records = []
    with open(path) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records