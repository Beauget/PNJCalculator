#DataGet

import requests
import json

def getT6JournalMage(): 
    dataRaw = requests.get("https://www.albion-online-data.com/api/v2/stats/Prices/T6_JOURNAL_MAGE_FULL?locations=Fortsterling&qualities=0")
    data = dataRaw.json()
    return data[0]['sell_price_min']
