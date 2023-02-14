#1~nまでのリストを作成する
def createList(n):
    lst = []
    for i in range(n+1):
        lst.append(i)
    lst.pop(0)
    return(lst)
