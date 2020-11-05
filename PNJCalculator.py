#PNJCalculator 

import os
import PySimpleGUI as ms



def rentability(values):


    headings = ['PNJ','Tier','Rentability','1/3']
    header = [[ms.Text(' ')] + [ms.Text(h,size=(14,1)) for h in headings]]
    res = values[0] * 2
    input_rows = [[ms.Text(res,size=(15,1), pad=(0,0)) for col in range(4)] for row in range(4)]

    layout1 = header + input_rows
    window = ms.Window('PNJRentability', layout1,margins=(200,200))
    window.read()


ms.theme("Dark")

#Stuff window
layout = [
    [ms.Text('Welcome to PNJCalculator')],
    [ms.Text('BlackSmith'),ms.InputText(size=(5,10)),ms.Text('Tier'),ms.Combo(['Tier4','Tier5','Tier6','Tier7','Tier8'])],
    [ms.Text('Imbuer'),ms.InputText(size=(5,10)),ms.Text('Tier'),ms.Combo(['Tier4','Tier5','Tier6','Tier7','Tier8'])],
    [ms.Text('Tinker'),ms.InputText(size=(5,10)),ms.Text('Tier'),ms.Combo(['Tier4','Tier5','Tier6','Tier7','Tier8'])],
    [ms.Text('Fletcher'),ms.InputText(size=(5,10)),ms.Text('Tier'),ms.Combo(['Tier4','Tier5','Tier6','Tier7','Tier8'])],
    [ms.Button('See rentability')]
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