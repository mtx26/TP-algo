listA = [2, 4, 5, 8, 9]

def getIndex(myList, elem) :
    if len(myList) == 1 :

        if elem < myList[0]:
            return 0
        else :
            return 1
    
    else :
        middle = len(myList)//2
        if elem < myList[middle] :
            return getIndex(myList[:middle], elem)
        else :
            return middle + getIndex(myList[middle:], elem)

def insert(myList, indice, elem) :
    myList.append(0)
    i = len(myList) - 1
    while i > indice :
        myList[i] = myList[i-1]
        i = i - 1
    myList[indice] = elem
    return myList

indice = getIndex(listA, 7)

insert(listA, indice, 7)

print(listA)