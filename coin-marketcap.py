#!/usr/bin/python3

################
#  Emre OVUNC  #
################

from os       import system
from time     import sleep
from queue    import Queue
from requests import get

bitcoin_flag         = 1
bitcoin_cash_flag    = 0
ripple_flag          = 1
dash_flag            = 1
bitcoin_gold_flag    = 0
litecoin_flag        = 1
iota_flag            = 0
monero_flag          = 1
cardano_flag         = 0
eth_classic_flag     = 1
neo_flag             = 0
nem_flag             = 0
eos_flag             = 0
stellar_lumens_flag  = 0
zcash_flag           = 0
dogecoin_flag        = 1
lisk_flag            = 1
stratis_flag         = 1

total = bitcoin_flag + bitcoin_cash_flag + ripple_flag + dash_flag + bitcoin_gold_flag +\
        litecoin_flag + iota_flag + monero_flag + cardano_flag + eth_classic_flag +\
        neo_flag + nem_flag + eos_flag + stellar_lumens_flag + zcash_flag + dogecoin_flag +\
        lisk_flag + stratis_flag

coin_queue    = Queue()
receiver_mail = 'coin_marketcaps@emreovunc.com'
mail_data     = 'mail -s "Digital Coins" ' + receiver_mail
content       = ""

while True:

    all_coins = get('https://coinmarketcap.com/').text

    if bitcoin_flag == 1:
        bitcoin           = all_coins.split('BTC')[4]
        bitcoin_marketcap = bitcoin.split('td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        bitcoin_price     = bitcoin.split('<a href="/currencies/bitcoin/#markets" class="price"')[1].split('</a>')[0].split('" >$')[1].strip()
        coin_queue.put((bitcoin_marketcap, bitcoin_price))

    if bitcoin_cash_flag == 1:
        bitcoin_cash           = all_coins.split('BCH')[1]
        bitcoin_cash_marketcap = bitcoin_cash.split('td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        bitcoin_cash_price     = bitcoin_cash.split('<a href="/currencies/bitcoin-cash/#markets" class="price"')[1].split('</a>')[0].split('" >$')[1].strip()
        coin_queue.put((bitcoin_cash_marketcap, bitcoin_cash_price))

    if dash_flag == 1:
        dash            = all_coins.split('DASH')[1]
        dash_marketcap  = dash.split('td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        dash_price      = dash.split('<a href="/currencies/dash/#markets" class="price"')[1].split('</a>')[0].split('" >$')[1].strip()
        coin_queue.put((dash_marketcap, dash_price))

    if bitcoin_gold_flag == 1:
        bitcoin_gold           = all_coins.split('BTG')[1]
        bitcoin_gold_marketcap = bitcoin_gold.split('td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        bitcoin_gold_price     = bitcoin_gold.split('<a href="/currencies/bitcoin-gold/#markets" class="price"')[1].split('</a>')[0].split('" >$')[1].strip()
        coin_queue.put((bitcoin_gold_marketcap, bitcoin_gold_price))

    if ripple_flag == 1:
        ripple           = all_coins.split('XRP')[1]
        ripple_marketcap = ripple.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        ripple_price     = ripple.split('<a href="/currencies/ripple/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((ripple_marketcap, ripple_price))

    if litecoin_flag == 1:
        litecoin           = all_coins.split('LTC')[1]
        litecoin_marketcap = litecoin.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        litecoin_price     = litecoin.split('<a href="/currencies/litecoin/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((litecoin_marketcap, litecoin_price))

    if iota_flag == 1:
        iota           = all_coins.split('MIOTA')[1]
        iota_marketcap = iota.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        iota_price     = iota.split('<a href="/currencies/iota/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((iota_marketcap, iota_price))

    if monero_flag == 1:
        monero           = all_coins.split('XMR')[1]
        monero_marketcap = monero.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        monero_price     = monero.split('<a href="/currencies/monero/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((monero_marketcap, monero_price))

    if cardano_flag == 1:
        cardano           = all_coins.split('ADA')[1]
        cardano_marketcap = cardano.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        cardano_price     = cardano.split('<a href="/currencies/cardano/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((cardano_marketcap, cardano_price))

    if eth_classic_flag == 1:
        etc           = all_coins.split('ETC')[1]
        etc_marketcap = etc.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        etc_price     = etc.split('<a href="/currencies/ethereum-classic/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((etc_marketcap, etc_price))

    if neo_flag == 1:
        neo           = all_coins.split('NEO')[2]
        neo_marketcap = neo.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        neo_price     = neo.split('<a href="/currencies/neo/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((neo_marketcap, neo_price))

    if nem_flag == 1:
        nem           = all_coins.split('XEM')[1]
        nem_marketcap = nem.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        nem_price     = nem.split('<a href="/currencies/nem/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((nem_marketcap, nem_price))

    if eos_flag == 1:
        eos           = all_coins.split('EOS')[2]
        eos_marketcap = eos.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        eos_price     = eos.split('<a href="/currencies/eos/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((eos_marketcap, eos_price))

    if stellar_lumens_flag == 1:
        stellar_lumens           = all_coins.split('XLM')[1]
        stellar_lumens_marketcap = stellar_lumens.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        stellar_lumens_price     = stellar_lumens.split('<a href="/currencies/stellar/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((stellar_lumens_marketcap, stellar_lumens_price))

    if zcash_flag == 1:
        zcash           = all_coins.split('ZEC')[1]
        zcash_marketcap = zcash.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        zcash_price     = zcash.split('<a href="/currencies/zcash/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((zcash_marketcap, zcash_price))

    if dogecoin_flag == 1:
        doge            = all_coins.split('DOGE')[1]
        doge_marketcap  = doge.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        doge_price      = doge.split('<a href="/currencies/dogecoin/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((doge_marketcap, doge_price))

    if lisk_flag == 1:
        lisk            = all_coins.split('LSK')[1]
        lisk_marketcap  = lisk.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        lisk_price      = lisk.split('<a href="/currencies/lisk/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((lisk_marketcap, lisk_price))

    if stratis_flag == 1:
        stratis             = all_coins.split('STRAT')[1]
        stratis_marketcap   = stratis.split('<td class="no-wrap market-cap text-right"')[1].split('" >')[1].strip().split('</td>')[0].strip()
        stratis_price       = stratis.split('<a href="/currencies/stratis/#markets" class="price" data-usd')[1].split('</a>')[0].split('" >')[1].strip()
        coin_queue.put((stratis_marketcap, stratis_price))

    if coin_queue.qsize() == total:
        pass

    elif coin_queue.qsize() == total*2:
        if bitcoin_flag == 1:
            coin = coin_queue.get()
            content += '##### BITCOIN #####\n'
            content += 'BTC MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(bitcoin_marketcap)[1:] + '\n'
            content += 'BTC Price      : ' + str(coin[1])     + ' - ' + str(bitcoin_price) + '\n'
            content += '###################\n\n'

        if bitcoin_cash_flag == 1:
            coin = coin_queue.get()
            content += '##### BITCOIN CASH #####\n'
            content += 'BCH MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(bitcoin_cash_marketcap)[1:] + '\n'
            content += 'BCH Price      : ' + str(coin[1])     + ' - ' + str(bitcoin_cash_price) + '\n'
            content += '########################\n\n'

        if dash_flag == 1:
            coin = coin_queue.get()
            content += '#####  DASH  #####\n'
            content += 'DASH MarketCap : ' + str(coin[0])[1:] + ' - ' + str(dash_marketcap)[1:] + '\n'
            content += 'DASH Price     : ' + str(coin[1])     + ' - ' + str(dash_price) + '\n'
            content += '###################\n\n'

        if bitcoin_gold_flag == 1:
            coin = coin_queue.get()
            content += '##### BITCOIN GOLD #####\n'
            content += 'BTG MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(bitcoin_gold_marketcap)[1:] + '\n'
            content += 'BTG Price      : ' + str(coin[1])     + ' - ' + str(bitcoin_gold_price) + '\n'
            content += '########################\n\n'

        if ripple_flag == 1:
            coin = coin_queue.get()
            content += '#####   XRP  #####\n'
            content += 'XRP MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(ripple_marketcap)[1:] + '\n'
            content += 'XRP Price      : ' + str(coin[1])[1:] + ' - ' + str(ripple_price)[1:] + '\n'
            content += '###################\n\n'

        if litecoin_flag == 1:
            coin = coin_queue.get()
            content += '#####   LTC  #####\n'
            content += 'LTC MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(litecoin_marketcap)[1:] + '\n'
            content += 'LTC Price      : ' + str(coin[1])[1:] + ' - ' + str(litecoin_price)[1:] + '\n'
            content += '###################\n\n'

        if iota_flag == 1:
            coin = coin_queue.get()
            content += '#####  MIOTA  #####\n'
            content += 'MIOTA MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(iota_marketcap)[1:] + '\n'
            content += 'MIOTA Price      : ' + str(coin[1])[1:] + ' - ' + str(iota_price)[1:] + '\n'
            content += '###################\n\n'

        if monero_flag == 1:
            coin = coin_queue.get()
            content += '#####   XMR  #####\n'
            content += 'XMR MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(monero_marketcap)[1:] + '\n'
            content += 'XMR Price      : ' + str(coin[1])[1:] + ' - ' + str(monero_price)[1:] + '\n'
            content += '###################\n\n'

        if cardano_flag == 1:
            coin = coin_queue.get()
            content += '#####  ADA  #####\n'
            content += 'ADA MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(cardano_marketcap)[1:] + '\n'
            content += 'ADA Price      : ' + str(coin[1])[1:] + ' - ' + str(cardano_price)[1:] + '\n'
            content += '##################\n\n'

        if eth_classic_flag == 1:
            coin = coin_queue.get()
            content += '#####   ETC  #####\n'
            content += 'ETC MarketCap  : ' + str(coin[0])[1:] + ' - ' + str(etc_marketcap)[1:] + '\n'
            content += 'ETC Price      : ' + str(coin[1])[1:] + ' - ' + str(etc_price)[1:] + '\n'
            content += '###################\n\n'

        if neo_flag == 1:
            coin = coin_queue.get()
            content += '#####  NEO  #####\n'
            content += 'NEO MarketCap : ' + str(coin[0])[1:] + ' - ' + str(neo_marketcap)[1:] + '\n'
            content += 'NEO Price     : ' + str(coin[1])[1:] + ' - ' + str(neo_price)[1:] + '\n'
            content += '##################\n\n'

        if nem_flag == 1:
            coin = coin_queue.get()
            content += '#####  XEM  #####\n'
            content += 'XEM MarketCap : ' + str(coin[0])[1:] + ' - ' + str(nem_marketcap)[1:] + '\n'
            content += 'XEM Price     : ' + str(coin[1])[1:] + ' - ' + str(nem_price)[1:] + '\n'
            content += '##################\n\n'

        if eos_flag == 1:
            coin = coin_queue.get()
            content += '#####  EOS  #####\n'
            content += 'EOS MarketCap : ' + str(coin[0])[1:] + ' - ' + str(eos_marketcap)[1:] + '\n'
            content += 'EOS Price     : ' + str(coin[1])[1:] + ' - ' + str(eos_price)[1:] + '\n'
            content += '##################\n\n'

        if stellar_lumens_flag == 1:
            coin = coin_queue.get()
            content += '#####  XLM  #####\n'
            content += 'XLM MarketCap : ' + str(coin[0])[1:] + ' - ' + str(stellar_lumens_marketcap)[1:] + '\n'
            content += 'XLM Price     : ' + str(coin[1])[1:] + ' - ' + str(stellar_lumens_price)[1:] + '\n'
            content += '##################\n\n'

        if zcash_flag == 1:
            coin = coin_queue.get()
            content += '#####  ZEC  #####\n'
            content += 'ZEC MarketCap : ' + str(coin[0])[1:] + ' - ' + str(zcash_marketcap)[1:] + '\n'
            content += 'ZEC Price     : ' + str(coin[1])[1:] + ' - ' + str(zcash_price)[1:] + '\n'
            content += '##################\n\n'

        if dogecoin_flag == 1:
            coin = coin_queue.get()
            content += '#####  DOGE  #####\n'
            content += 'DOGE MarketCap : ' + str(coin[0])[1:] + ' - ' + str(doge_marketcap)[1:] + '\n'
            content += 'DOGE Price     : ' + str(coin[1])[1:] + ' - ' + str(doge_price)[1:] + '\n'
            content += '###################\n\n'

        if lisk_flag == 1:
            coin = coin_queue.get()
            content += '#####  LISK  #####\n'
            content += 'LISK MarketCap : ' + str(coin[0])[1:] + ' - ' + str(lisk_marketcap)[1:] + '\n'
            content += 'LISK Price     : ' + str(coin[1])[1:] + ' - ' + str(lisk_price)[1:] + '\n'
            content += '###################\n\n'

        if stratis_flag == 1:
            coin = coin_queue.get()
            content += '#####  STRAT  #####\n'
            content += 'STRAT MarketCap : ' + str(coin[0])[1:] + ' - ' + str(stratis_marketcap)[1:] + '\n'
            content += 'STRAT Price     : ' + str(coin[1])[1:] + ' - ' + str(stratis_price)[1:] + '\n'
            content += '###################\n\n'

        system('echo "' + str(content) + '" | ' + str(mail_data))

        content = ""

    else:
        while coin_queue.qsize():
            coin_queue.get()

    sleep(5)
