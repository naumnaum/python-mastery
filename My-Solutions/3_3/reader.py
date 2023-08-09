import csv
import collections
import collections.abc

class RideData(collections.abc.Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []      
        self.dates = []
        self.daytypes = []
        self.numrides = []
    
    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, slice):
            sliced_data = RideData()
            start, stop, step = index.start, index.stop, index.step
            if step is None: step = 1
            for i in range(start, stop, step):
                row = { 
                    'route': self.routes[i],
                    'date': self.dates[i],
                    'daytype': self.daytypes[i],
                    'rides': self.numrides[i] }
                sliced_data.append(row)
            return(sliced_data)
        else:             
            return { 'route': self.routes[index],
                    'date': self.dates[index],
                    'daytype': self.daytypes[index],
                    'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

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