#PNJCalculator 

import os
import data as need
import json
import PySimpleGUI as ms
import requests







#https://www.albion-online-data.com/api/v2/stats/View/T2_FARM_BEAN_SEED?locations=FORTSTRELING&qualities=0

def rentability(values):

    city = values['City']
    BlackSmith = values['BlacksmithNumber']
    #BlackSmith treatment
    result = {}

    if values['BlacksmithTier'] == 'Tier4':
        result = need.getT4Data(city)
    elif values['BlacksmithTier'] == 'Tier5':
         result = need.getT5Data(city)
    elif values['BlacksmithTier'] == 'Tier6':
         result = need.getT6Data(city)
    elif values['BlacksmithTier'] == 'Tier7':
         result = need.getT7Data(city)
    elif values['BlacksmithTier'] == 'Tier8':
         result = need.getT8Data(city)
    else:
        print("aled")
    headings = ['PNJ','Tier','Rentability','1/3']
    header = [[ms.Text(' ')] + [ms.Text(h,size=(14,1)) for h in headings]]
    input_rows = [[ms.Text(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(4)]

    layout1 = header + input_rows
    window = ms.Window('PNJRentability', layout1,margins=(200,200))
    window.read()


ms.theme("Dark")

#Stuff window
layout = [
    [ms.Text('Welcome to PNJCalculator')],
    [ms.Text('BlackSmith'),ms.InputText(size=(5,10),key='BlacksmithNumber'),ms.Text('Tier'),ms.Combo(['Tier4','Tier5','Tier6','Tier7','Tier8'],key='BlacksmithTier')],
    [ms.Text('Imbuer'),ms.InputText(size=(5,10),key='ImbuerNumber'),ms.Text('Tier'),ms.Combo(['Tier4','Tier5','Tier6','Tier7','Tier8'],key='ImbuerTier')],
    [ms.Text('Tinker'),ms.InputText(size=(5,10),key='TinkerNumber'),ms.Text('Tier'),ms.Combo(['Tier4','Tier5','Tier6','Tier7','Tier8'],key='TinkerTier')],
    [ms.Text('Fletcher'),ms.InputText(size=(5,10),key='FletcherNumber'),ms.Text('Tier'),ms.Combo(['Tier4','Tier5','Tier6','Tier7','Tier8'],key='FletcherTier')],
    [ms.Button('See rentability'),ms.Text('City'),ms.Combo(['Fortsterling','Martlock','Lymhurst','Bridgewatch','Thetford','Caerleon'],key='City')]
]

window = ms.Window('PNJCalculator', layout,margins=(200,200))

while True:
    event, values  = window.read()
    if event == 'See rentability':
        rentability(values)

    #End program
    if event == ms.WIN_CLOSED:
        break



window.close()