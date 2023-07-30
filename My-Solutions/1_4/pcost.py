import sys

def portfolio_cost(filename):
    f = open(str(filename), "r")
    total_portfolio_cost = 0.0
    for line in f:
        line_list = line.split()
        try: 
            num_shares = int(line_list[1])
        except Exception as e:
            print(f"Reason: {e}")
        try:
            prices_per_share = float(line_list[2])
        except Exception as e:
            print(f"Reason: {e}")
        total_portfolio_cost += num_shares * prices_per_share
    print(total_portfolio_cost)

if __name__ == '__main__':
    print(sys.argv)
    
    portfolio_cost(sys.argv[1])
    