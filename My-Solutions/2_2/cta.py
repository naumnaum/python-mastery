from readrides import read_rides_as_dicts
from collections import defaultdict, Counter

# 1. How many bus routes exist in Chicago
rows = read_rides_as_dicts()
unique_routes = { row['route'] for row in rows }
print(f"There's {len(unique_routes)} unique routes in Chicago")

# 2.1. How many people rode the number 22 bus on February 2, 2011? 
# 2.2. What about any route on any date of your choosing?
byroute = defaultdict(list)
for row in rows:
    byroute[row['route']].append(row)

route = '22'
date = '02/02/2011'
total_route_date = 0
for record in byroute[route]:
    if (record['date'] == date):
        total_route_date += record['rides']

print(f"There was {total_route_date} rides on route {route} on {date}")

# 3. What is the total number of rides taken on each bus route?
route_totals = {}
for name in byroute:
    route_total = 0
    for record in byroute[name]:
        route_total += record['rides']
    route_totals[name] = route_total

# print(route_totals)

# 4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
# First let's create a dict {'route': '2001': num_rides, ..., '2011': num_rides}
route_year_totals = {}
for name in byroute:
    year_totals = Counter()
    for row in byroute[name]:
        day, month, year = row['date'].split('/')
        year_totals[year] += row['rides']
    route_year_totals[name] = year_totals

# And now let's iterate through created dict
# And create a new list: {'route': rides_total_2011 - rides_total_2001}
rides_increase_total = Counter()
year_start = '2001'
year_end = '2011'
for name in route_year_totals:
    try: 
        total_start = route_year_totals[name][year_start]
        total_end = route_year_totals[name][year_end]
        increase_total = total_end - total_start
        rides_increase_total[name] = increase_total
    except:
        print(f"That bus was not working in {year_start}")

print(rides_increase_total.most_common(1))