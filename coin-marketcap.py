#!/usr/bin/python3

################
#  Emre OVUNC  #
################

from os import system
from time import sleep
from queue import Queue
from requests import get

coin_queue    = Queue()
receiver_mail = 'coin_marketcaps@emreovunc.com'
mail_data     = 'mail -s "Digital Coins" ' + receiver_mail
content       = ""

while True:

    all_coins = get('https://coinmarketcap.com/').text

    bitcoin           = all_coins.split('BTC')[4]
    bitcoin_marketcap = bitcoin.split('td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
    bitcoin_price     = bitcoin.split('<a href="/currencies/bitcoin/#markets" class="price"')[1].split('</a>')[0].split('" >$')[1].strip()

    coin_queue.put((bitcoin_marketcap, bitcoin_price))

    dash            = all_coins.split('DASH')[1]
    dash_marketcap  = dash.split('td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
    dash_price      = dash.split('<a href="/currencies/dash/#markets" class="price"')[1].split('</a>')[0].split('" >$')[1].strip()

    coin_queue.put((dash_marketcap, dash_price))

    doge            = all_coins.split('DOGE')[1]
    doge_marketcap  = doge.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
    doge_price      = doge.split('<a href="/currencies/dogecoin/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()

    coin_queue.put((doge_marketcap, doge_price))

    etc             = all_coins.split('ETC')[1]
    etc_marketcap   = etc.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
    etc_price       = etc.split('<a href="/currencies/ethereum-classic/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()

    coin_queue.put((etc_marketcap, etc_price))

    lisk            = all_coins.split('LSK')[1]
    lisk_marketcap  = lisk.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
    lisk_price      = lisk.split('<a href="/currencies/lisk/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()

    coin_queue.put((lisk_marketcap, lisk_price))

    litecoin            = all_coins.split('LTC')[1]
    litecoin_marketcap  = litecoin.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
    litecoin_price      = litecoin.split('<a href="/currencies/litecoin/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()

    coin_queue.put((litecoin_marketcap, litecoin_price))

    stratis             = all_coins.split('STRAT')[1]
    stratis_marketcap   = stratis.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
    stratis_price       = stratis.split('<a href="/currencies/stratis/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()

    coin_queue.put((stratis_marketcap, stratis_price))

    monero              = all_coins.split('XMR')[1]
    monero_marketcap    = monero.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
    monero_price        = monero.split('<a href="/currencies/monero/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()

    coin_queue.put((monero_marketcap, monero_price))

    ripple           = all_coins.split('XRP')[1]
    ripple_marketcap = ripple.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
    ripple_price     = ripple.split('<a href="/currencies/ripple/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()

    coin_queue.put((ripple_marketcap, ripple_price))

    if coin_queue.qsize() == 9:
        pass

    elif coin_queue.qsize() == 18:
        coin = coin_queue.get()
        content += '##### BITCOIN #####\n'
        content += 'BTC MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(bitcoin_marketcap)[1:] + '\n'
        content += 'BTC Price      : ' + str(coin[1])     + ' - ' + str(bitcoin_price) + '\n'
        content += '###################\n\n'

        coin = coin_queue.get()
        content += '#####  DASH  #####\n'
        content += 'DASH MarketCap : ' + str(coin[0])[1:] + ' - ' + str(dash_marketcap)[1:] + '\n'
        content += 'DASH Price     : ' + str(coin[1])     + ' - ' + str(dash_price) + '\n'
        content += '###################\n\n'

        coin = coin_queue.get()
        content += '#####  DOGE  #####\n'
        content += 'DOGE MarketCap : ' + str(coin[0])[1:] + ' - ' + str(doge_marketcap)[1:] + '\n'
        content += 'DOGE Price     : ' + str(coin[1])[1:] + ' - ' + str(doge_price)[1:] + '\n'
        content += '###################\n\n'

        coin = coin_queue.get()
        content += '#####   ETC  #####\n'
        content += 'ETC MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(etc_marketcap)[1:] + '\n'
        content += 'ETC Price      : ' + str(coin[1])[1:] + ' - ' + str(etc_price)[1:] + '\n'
        content += '###################\n\n'

        coin = coin_queue.get()
        content += '#####  LISK  #####\n'
        content += 'LISK MarketCap : ' + str(coin[0])[1:] + ' - ' + str(lisk_marketcap)[1:] + '\n'
        content += 'LISK Price     : ' + str(coin[1])[1:] + ' - ' + str(lisk_price)[1:] + '\n'
        content += '###################\n\n'

        coin = coin_queue.get()
        content += '#####   LTC  #####\n'
        content += 'LTC MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(litecoin_marketcap)[1:] + '\n'
        content += 'LTC Price      : ' + str(coin[1])[1:] + ' - ' + str(litecoin_price)[1:] + '\n'
        content += '###################\n\n'

        coin = coin_queue.get()
        content += '#####  STRAT  #####\n'
        content += 'STRAT MarketCap : ' + str(coin[0])[1:] + ' - ' + str(stratis_marketcap)[1:] + '\n'
        content += 'STRAT Price     : ' + str(coin[1])[1:] + ' - ' + str(stratis_price)[1:] + '\n'
        content += '###################\n\n'

        coin = coin_queue.get()
        content += '#####   XMR  #####\n'
        content += 'XMR MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(monero_marketcap)[1:] + '\n'
        content += 'XMR Price      : ' + str(coin[1])[1:] + ' - ' + str(monero_price)[1:] + '\n'
        content += '###################\n\n'

        coin = coin_queue.get()
        content += '#####   XRP  #####\n'
        content += 'XRP MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(ripple_marketcap)[1:] + '\n'
        content += 'XRP Price      : ' + str(coin[1])[1:] + ' - ' + str(ripple_price)[1:] + '\n'
        content += '###################\n\n'

        system('echo "' + str(content) + '" | ' + str(mail_data))

        content = ""

    else:
        while coin_queue.qsize():
            coin_queue.get()

    sleep(1200)
