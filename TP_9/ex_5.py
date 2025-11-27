list = [5, 6, 3, 2, 1]

def bubble_sort(list):
    n = len(list)
    is_sorted = False

    while not is_sorted:
        modify = False

        for i in range(n-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                modify = True
            
        if not modify:
            is_sorted = True
    
    return(list)

if __name__ == "__main__":
    print(bubble_sort(list))