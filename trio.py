#trio.py - 3連複を表示するアプリ
import random as rd #ランダムに3つ選ぶのに使用

def trio(number_of_starters): #リストを渡してください
    if len(number_of_starters) > 2:
        tierces = rd.sample(number_of_starters, 3) #listsから３つランダムで選ぶ
        txt = f'{tierces[0]}-{tierces[1]}-{tierces[2]}' #表示するテキストを作る
        return txt
    else:
        txt = '頭数が少なすぎます。'
        return txt