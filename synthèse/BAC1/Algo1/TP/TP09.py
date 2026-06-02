import sort
import umons_cpu
import displayCpu


def bubble_sort(list):
    flag = True
    while flag :
        cnt = 0
        i = 0
        while i < (len(list) - 1) :
            if list[i] > list[i+1] :
                cnt = cnt + 1
                (list[i],list[i+1]) = (list[i+1],list[i])
            i = i + 1
        if cnt == 0 :
            flag = False
    return list


#print(bubble_sort([5,4,3,2,1]))
#print(bubble_sort([5,2,4,3,1]))

            