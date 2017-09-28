from coinbase.wallet.client import Client

def login(key, secret):
    client = Client(key, secret)
    return client

def getBalances(client, wallet='all', how='native', show=False):
    '''
    Uses a logged in client to check the specified wallet's balance in the specified currency. If a wallet is 'all' and
    how is 'native', then the value retured will be the sum of all wallets value on coinbase, in native currency
    :param client:
    :param wallet:
    :param how:
    :return:
    '''
    if show:
        print('--Coinbase------------------------------')
    if how == 'native':
        native_value = 0
        if wallet == 'all':
            for account in client.get_accounts().data:
                native_value += float(account.native_balance.amount)
                balance = float(account.balance.amount)
                if show:
                    print('\t{}\t{}\t\t${}'.format(account['currency'], round(balance,5),round(float(account.native_balance.amount),2)))
        else:
            account = client.get_account(wallet)
            native_value += account.native_balance.amount
        return native_value
