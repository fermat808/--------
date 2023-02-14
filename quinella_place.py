#quinella_place.py - ワイドを表示する

import random as rd #ランダムに3つ選ぶのに使用

def quinella_place(number_of_starters): #リストを渡してください
    if len(number_of_starters) > 1:
        length = len(number_of_starters) #int型
        e = rd.sample(number_of_starters, 2) #listsから３つランダムで選ぶ
        txt = f'{e[0]}-{e[1]}' #表示するテキストを作る
        return txt
    else:
        txt = '頭数が少なすぎます。'
        return txt