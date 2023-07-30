f = open("/Users/alexeynaumov/Desktop/python-mastery/Data/portfolio.dat", "r")
total_portfolio_cost = 0.0
for line in f:
    line_list = line.split()
    total_portfolio_cost += int(line_list[1]) * float(line_list[2])
print(total_portfolio_cost)
    