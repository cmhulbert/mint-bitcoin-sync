import gdax

def login(key, secret, passphrase):
    client = gdax.AuthenticatedClient(key, secret, passphrase)
    return client

def getBalances(client, wallet='all', how='native', show=False):
    '''
    Uses a logged in client to check the specified wallet's balance in the specified currency. If a wallet is 'all' and
    how is 'native', then the value retured will be the sum of all wallets value on coinbase, in native currency.
    Currently no other functionality is suppoted
    :param client:
    :param wallet:
    :param how:
    :return:
    '''
    if show:
        print('--GDAX---------------------------------')
    native='USD'
    if how == 'native':
        native_value = 0
        if wallet == 'all':
            for account in client.get_accounts():
                currency = account['currency']
                native_balance = float(account['balance'])
                if currency != native:
                    ticker = client.get_product_ticker(currency + '-' + native)
                    native_exchange_rate = float(ticker['price'])
                    balance = native_balance
                    native_balance = balance*native_exchange_rate
                native_value += native_balance
                if show:
                    print('\t{}\t{}\t\t${}'.format(currency, round(balance,5), round(round(native_balance,2))))
        return native_value
