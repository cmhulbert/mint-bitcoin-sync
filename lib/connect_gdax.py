import gdax

def login(key, secret, passphrase):
    client = gdax.AuthenticatedClient(key, secret, passphrase)
    return client

def getBalances(client, wallet='all', how='native'):
    '''
    Uses a logged in client to check the specified wallet's balance in the specified currency. If a wallet is 'all' and
    how is 'native', then the value retured will be the sum of all wallets value on coinbase, in native currency.
    Currently no other functionality is suppoted
    :param client:
    :param wallet:
    :param how:
    :return:
    '''
    native='USD'
    if how == 'native':
        native_value = 0
        if wallet == 'all':
            for account in client.get_accounts():
                currency = account['currency']
                balance = account['balance']
                ticker = client.cet_product_ticker(currency + '-' + native)
                native_exchange_rate = balance * ticker['price']
                native_value += balance*native_exchange_rate
