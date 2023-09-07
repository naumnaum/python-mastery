# follow.py
import os
import time
# f = open('/Users/alexeynaumov/Desktop/python-mastery/Data/stocklog.csv')
# f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file
path = '/Users/alexeynaumov/Desktop/python-mastery/Data/stocklog.csv'

def follow(path):
    f = open(path)
    f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

# Example use
if __name__ == '__main__':
    for line in follow(path):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))