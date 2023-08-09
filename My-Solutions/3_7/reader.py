import csv
import collections
import collections.abc
from abc import ABC, abstractmethod

class CSVParser(ABC):

    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }
    
class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
    

def read_csv_as_dicts(filename, coltypes=list):
    '''
    Read the bus ride data as a list of dicts
    '''
    path = '../../Data/' + filename
    parser = DictCSVParser(coltypes)
    port = parser.parse(path)
    return port

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    path = '../../Data/' + filename
    parser = InstanceCSVParser(cls)
    port = parser.parse(path)
    return port