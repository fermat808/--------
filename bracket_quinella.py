#bracket_quinella.py - 枠連を表示するアプリ

import random as rd #ランダムに3つ選ぶのに使用

def bracket_quinella(number_of_starters): #リストを渡してください
    #頭数が１～８のとき
    if len(number_of_starters) < 9:
        txt = '頭数が少なすぎます。'
    #頭数が９～１５のとき
    else :
        lst = [1, 2, 3, 4, 5, 6, 7, 8]
        e = rd.choices(lst, k=2) #listsから３つランダムで選ぶ
        txt = f'{e[0]}-{e[1]}' #表示するテキストを作る
    return txt