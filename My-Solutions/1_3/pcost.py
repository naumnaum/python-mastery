# Loading the file
portfolio = open("/Users/alexeynaumov/Desktop/python-mastery/Data/portfolio.dat", "r")
# print(portfolio.read())
pr = portfolio.read()
pr_list = pr.split()
print(pr_list)

# Creating a prices dictionary
prices = {}
for i in range(0, len(pr_list), 3):
    print(f"{pr_list[i]} NUM SHARES: {pr_list[i+1]} PRICE: {pr_list[i+2]}")
    prices[pr_list[i]] = [int(pr_list[i+1]), float(pr_list[i+2])]
print(prices)

# Iterating through prices dictionary
total_portfolio_cost = 0.0 
for key, value in prices.items():
    # print("NUM SHARES: ", value[0])
    # print("PRICE: ", value[1])
    # print(f"COST PER COMPANY {key}: ", value[0] * value[1])
    total_portfolio_cost += value[0] * value[1]
print(total_portfolio_cost)