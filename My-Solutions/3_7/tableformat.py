from abc import ABC, abstractmethod

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

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

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end=' ')
        for h in headers:
            print('<th>%s</th>' % h, end=' ')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end=' ')
        for d in rowdata:
            print('<td>%s</td>' % d, end=' ')
        print('</tr>')

def create_formatter(type=str):
    if type == 'csv':
        return CSVTableFormatter()
    if type == 'text':
        return TextTableFormatter()
    if type == 'html':
        return HTMLTableFormatter()
    else:
        return NotImplementedError()

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

