def getIndex(myList, elem):
    if len(myList) == 1 :
        if elem < myList[0]:
            return 0
        else :
            return 1
    else :
        mid = len(myList)//2
        if elem < myList[mid]:
            return getIndex(myList[:mid], elem)
        else :
            return mid + getIndex(myList[mid:], elem)
        
def insert(myList, indice, elem):
    myList.append(elem)
    i = len(myList) - 1
    while myList[indice] != elem :
        (myList[i], myList[i-1]) = (myList[i-1], myList[i])
        i = i - 1
    return myList


        