from abc import ABC, abstractmethod

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        header = ' '.join('%10s' % name for name in headers)
        print(header)
        print('-' * len(header))

    def row(self, rowdata):
        row = ' '.join('%10s' % d for d in rowdata)
        print(row)

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        header = ','.join(name for name in headers)
        print(header)

    def row(self, rowdata):
        row = ','.join(str(d) for d in rowdata)
        print(row)

def create_formatter(type=str):
    if type == 'csv':
        return CSVTableFormatter()
    if type == 'text':
        return TextTableFormatter()
    else:
        return NotImplementedError()

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

