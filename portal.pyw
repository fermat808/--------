import PySimpleGUI as sg
from win import win #単勝
from place import place #複勝
from exacta import exacta #馬単
from quinella import quinella #馬連
from tierce import tierce #3連単
from trio import trio #3連複
from quinella_place import quinella_place #ワイド
from bracket_quinella import bracket_quinella #枠連
from create_number_lists import createList #１～ｎまでのリストを返す

#頭数のリスト
entries = [1, 2, 3, 4, 5,
           6, 7, 8, 9, 10,
           11, 12, 13, 14, 15,
           16, 17, 18]

#買い方のリスト
selections =['単勝', '複勝', '馬単', '馬連', '馬単',
             'ワイド', '枠連', '３連複', '３連単']

#layoutをつくる
layout = [[sg.Text('頭数を選んでください。', key='txt1'), sg.Text('買い方を選んでください。', key='txt2')],
          [sg.Listbox(entries, size=(None, 3), key='lb'), sg.Listbox(selections, size=(None, 3), key='sl')],
          [sg.Button('選択', key='btn')],
          [sg.Text('', key='txt3')],]
window = sg.Window('競馬アプリ', layout, size=(450, 150))

#アプリの仕組み
while True:
    event, values = window.read()
    while event == 'btn':
        #try節を挿入する
        if values['lb'] and values['sl']:
            e = values['lb'].pop(0) #ここであかんくなった
            f = values['sl'].pop(0)
            e1 = createList(e)
            if f == '単勝':
                txt = win(e1)
                window['txt3'].update(txt)
                break
            if f == '複勝':
                txt = place(e1)
                window['txt3'].update(txt)
                break
            if f == '馬単':
                txt = exacta(e1)
                window['txt3'].update(txt)
                break
            if f == '馬連':
                txt = quinella(e1)
                window['txt3'].update(txt)
                break
            if f == '３連複':
                txt = trio(e1)
                window['txt3'].update(txt)
                break
            if f == '３連単':
                txt = tierce(e1)
                window['txt3'].update(txt)
                break
            if f == 'ワイド':
                txt = quinella_place(e1)
                window['txt3'].update(txt)
                break
            if f == '枠連':
                txt = bracket_quinella(e1)
                window['txt3'].update(txt)
                break
        else:
            break
    if event == None:
            break
    
window.close()