import lib.connect_gdax as lcg
import lib.connect_coinbase as lcc


def main():
    with open('api_info.local', 'r') as f:
        cb = f.readline().strip()
        cb = cb.split('    ')
        gd = f.readline().strip()
        gd = gd.split('    ')

    coinbase_client = lcc.login(cb[0], cb[1])
    gdax_client = lcg.login(gd[0], gd[1], gd[2])


    coinbase_balance = lcc.getBalances(coinbase_client, show=True)
    gdax_balance = lcg.getBalances(gdax_client, show=True)
    aggregate_balance = coinbase_balance + gdax_balance
    print('\nCoinbase:\t{:.2f}\nGDAX:\t\t{:.2f}\nSum:\t\t{:.2f}'.format(coinbase_balance, gdax_balance, aggregate_balance))

if __name__ == '__main__':
    main()