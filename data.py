#DataGet

import requests
import json

def getT4Data(city): 
    #BooksData
    result = {}
    data = requests.get("https://www.albion-online-data.com/api/v2/stats/Prices/T4_JOURNAL_MAGE_EMPTY?locations="+city+"&qualities=0")
    data2 = requests.get("https://www.albion-online-data.com/api/v2/stats/Prices/T4_JOURNAL_MAGE_FULL?locations="+city+"&qualities=0")
    emptyBookPrice = data.json()
    fullBookPrice = data2.json()
    result["emptyBookPrice"] = emptyBookPrice[0]['sell_price_min']
    result["fullBookPrice"] = fullBookPrice[0]['sell_price_min']

    #RessourcesData
    T4bar = requests.get("https://www.albion-online-data.com/api/v2/stats/Prices/T4_METALBAR?locations="+city+"&qualities=0")
    T4barPrice = T4bar.json()
    T4bar1 =  requests.get("https://www.albion-online-data.com/api/v2/stats/Prices/T4_METALBAR_LEVEL1@1?locations="+city+"&qualities=0")
    T4bar1Price = T4bar1.json()
    T4bar2 =  requests.get("https://www.albion-online-data.com/api/v2/stats/Prices/T4_METALBAR_LEVEL2@2?locations="+city+"&qualities=0")
    T4bar2Price = T4bar2.json()
    T4bar3 =  requests.get("https://www.albion-online-data.com/api/v2/stats/Prices/T4_METALBAR_LEVEL3@3?locations="+city+"&qualities=0")
    T4bar3Price = T4bar3.json()


    result["T4bar"] = T4barPrice[0]['sell_price_min']
    result["T4bar1"] = T4bar1Price[0]['sell_price_min']
    result["T4bar2"] = T4bar2Price[0]['sell_price_min']
    result["T4bar3"] = T4bar3Price[0]['sell_price_min']


    return result


def getT5Data(city): 
    dataRaw = requests.get("https://www.albion-online-data.com/api/v2/stats/Prices/T6_JOURNAL_MAGE_FULL?locations=Fortsterling&qualities=0")
    data = dataRaw.json()
    return data[0]['sell_price_min']


def getT6Data(city): 
    dataRaw = requests.get("https://www.albion-online-data.com/api/v2/stats/Prices/T6_JOURNAL_MAGE_FULL?locations=Fortsterling&qualities=0")
    data = dataRaw.json()
    return data[0]['sell_price_min']

def getT7Data(city): 
    dataRaw = requests.get("https://www.albion-online-data.com/api/v2/stats/Prices/T6_JOURNAL_MAGE_FULL?locations=Fortsterling&qualities=0")
    data = dataRaw.json()
    return data[0]['sell_price_min']

def getT8Data(city): 
    dataRaw = requests.get("https://www.albion-online-data.com/api/v2/stats/Prices/T6_JOURNAL_MAGE_FULL?locations=Fortsterling&qualities=0")
    data = dataRaw.json()
    return data[0]['sell_price_min']
