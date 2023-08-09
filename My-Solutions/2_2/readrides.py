import csv
import sys
from collections import namedtuple

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

def read_rides_as_dicts(filename='/Users/alexeynaumov/Desktop/python-mastery/Data/ctabus.csv'):
    '''
    Read the bus ride data as a list of dicts
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
            record = {
                'route': route, 
                'date': date, 
                'daytype': daytype, 
                'rides' : rides
                }
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


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    print(sys.argv)
    filename = '/Users/alexeynaumov/Desktop/python-mastery/Data/ctabus.csv'
    if sys.argv[1] == 'tuple':
        rows = read_rides_as_tuples(filename)
    if sys.argv[1] == 'dict':
        rows = read_rides_as_dict(filename)
    if sys.argv[1] == 'class':
        rows = read_rides_as_class(filename)
    if sys.argv[1] == 'namedtuple':
        rows = read_rides_as_namedtuple(filename)
    if sys.argv[1] == 'class_slots':
        rows = read_rides_as_class_slots(filename)
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())