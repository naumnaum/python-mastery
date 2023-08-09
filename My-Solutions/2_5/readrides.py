import csv
import sys
from collections import namedtuple
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
    

def read_rides_as_dicts(filename='/Users/alexeynaumov/Desktop/python-mastery/Data/ctabus.csv'):
    '''
    Read the bus ride data as a list of dicts
    '''
    # records = []
    records = RideData() # If you want to read data as columns
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route, 
                'date': date, 
                'daytype': daytype, 
                'rides' : rides
                }
            records.append(record)
    return records


def read_rides_as_tuples(filename='/Users/alexeynaumov/Desktop/python-mastery/Data/ctabus.csv'):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_class(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route=route, date=date, daytype=daytype, rides=rides)
            records.append(record)
        return records

def read_rides_as_namedtuple(filename):
    records = []
    Row_namedtuple = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row_namedtuple(route, date, daytype, rides)
            records.append(record)
        return records

class Row_slots:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_class_slots(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row_slots(route=route, date=date, daytype=daytype, rides=rides)
            records.append(record)
        return records

def read_rides_as_columns(filename = '/Users/alexeynaumov/Desktop/python-mastery/Data/ctabus.csv'):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

# if __name__ == '__main__':
    # import tracemalloc
    # tracemalloc.start()
    # print(sys.argv)
    # filename = '/Users/alexeynaumov/Desktop/python-mastery/Data/ctabus.csv'
    # if sys.argv[1] == 'tuple':
    #     rows = read_rides_as_tuples(filename)
    # if sys.argv[1] == 'dict':
    #     rows = read_rides_as_dicts(filename)
    # if sys.argv[1] == 'class':
    #     rows = read_rides_as_class(filename)
    # if sys.argv[1] == 'namedtuple':
    #     rows = read_rides_as_namedtuple(filename)
    # if sys.argv[1] == 'class_slots':
    #     rows = read_rides_as_class_slots(filename)
    # print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    # print("What's up?")