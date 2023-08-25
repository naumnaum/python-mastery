
def parse_line(line):
    line_splitted = line.split(sep="=")
    if len(line_splitted) == 2:
        return tuple(line_splitted)
    else:
        return None
