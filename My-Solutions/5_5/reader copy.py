import csv
from typing import List, Dict, Type, Callable
import logging

def read_csv_as_dicts(filename: str, 
                      types: List[str], 
                      headers: List[str]=None) -> List[Dict]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    data_folder_path = "/Users/alexeynaumov/Desktop/python-mastery/Data/"
    filename = data_folder_path + filename
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)
    
def read_csv_as_instances(filename: str, 
                          cls: Type, 
                          headers: List[str]=None) -> List[Type]:
    '''
    Read CSV data into a list of instances
    '''
    data_folder_path = "/Users/alexeynaumov/Desktop/python-mastery/Data/"
    filename = data_folder_path + filename
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)

def csv_as_dicts(lines: Type, 
                 types: List[Type],
                 *, 
                 headers: List[str]=None) -> List[Dict]:
    '''
    Read lines of data data into a list of dictionaries with optional type conversion
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        headers = next(rows)

    for idx, row in enumerate(rows):
        try:
            record = { name: func(val) 
                        for name, func, val in zip(headers, types, row) }
            records.append(record)
        except Exception as e:
            exc_msg = str(e)
            logging.warning(f"Row {idx}: Bad row: {row}")
            logging.debug(f"Row {idx}:, Message: {exc_msg}")
    return records

def csv_as_instances(lines: Type, 
                     cls: Type, 
                     *, 
                     headers: List[str]=None) -> List[Type]:
    '''
    Read lines of data into a list of instances
    '''
    records = []
    rows = csv.reader(lines)
    
    if headers is None:
        headers = next(rows)

    for idx, row in enumerate(rows):
        try:
            record = cls.from_row(row)
            records.append(record)
        
        except Exception as e:
            exc_msg = str(e)
            logging.warning(f"Row {idx}: Bad row: {row}")
            logging.debug(f"Row {idx}:, Message: {exc_msg}")
    return records

def convert_csv(lines: Type, 
                converter: Callable,
                *, 
                headers: List[str]=None) -> List[Type]:
    '''
    Read lines of data by converting 
    them with user-defined function 'converter'
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
        
    records = list(map(lambda row: converter(headers, row), rows))
    return records
