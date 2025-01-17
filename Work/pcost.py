# pcost.py

import Work.report2 as report
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)
    # return sum([s['shares'] * s['price'] for s in portfolio])
    return portfolio.total_cost


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))


if __name__ == '__main__':
    import sys
    main(sys.argv)

# main(["pcost.py", "Work/Data/portfolio.csv"])


# import sys
# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = "Work/Data/portfolio.csv"
# cost = portfolio_cost(filename)
# print('Total cost:', cost)




















