
def print_table(table, fields):
    header = ' '.join('%10s' % name for name in fields)
    print(header)
    print('-' * len(header))
    for l in table:
        row = ' '.join('%10s' % str(getattr(l, name)) for name in fields)
        print(row)

