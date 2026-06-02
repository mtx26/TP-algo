def rech_dic_ite(myTuple, elem):
    flag = True
    while flag :
        middle = len(myTuple) // 2
        if middle == 0 and elem != myTuple[middle] :
            flag = False
        if elem == myTuple[middle] :
            return True
        elif elem > myTuple[middle] :
            myTuple = myTuple[middle +1 :]
        else :
            myTuple = myTuple[:middle]
    return False
    
print(rech_dic_ite((0,1,2,3,5,7,9,11), 6))

    
