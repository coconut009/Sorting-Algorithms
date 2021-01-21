def selection_sort(num_arry):
    length = len(num_arry)

    for i in range (length):
        min_value_index =i

        for j in range (i, length):
            if num_arry[j] < num_arry[min_value_index]:
                min_value_index = j

        if min_value_index != i:
                num_arry[min_value_index], num_arry[i] = num_arry[i], num_arry[min_value_index]
    
    return num_arry

def quick_sort(num_arry):
    length = len(num_arry)
    if length <=1:
        return num_arry
    else:
        pivot = num_arry.pop()

    
    items_greater = []
    items_lower = []

    for item in num_arry:
        if item > pivot:
            items_greater.append(item)
        
        else:
            items_lower.append(item)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


def insertion_sort(num_arry):
    length =range(1,len(num_arry)) 
    for i in  length:
        value_to_sort = num_arry[i]

        while num_arry[i-1] > value_to_sort and i>0:
            num_arry[i], num_arry[i-1] = num_arry[i-1], num_arry[i]
            i=i-1
    return num_arry

def bubble_sort(num_arry):
    length = len(num_arry)
    value_sorted = False

    while not value_sorted:
        value_sorted = True
        for i in range (length-1):
            if  num_arry[i] > num_arry[i+1]:
                value_sorted = False
                num_arry[i],num_arry[i+1] = num_arry[i+1],num_arry[i]
    return num_arry


def heapify(num_arry,length,i):
    root_index   = i
    left_index   =  2*i + 1
    right_index   = 2*i + 2

    if left_index < length and num_arry[i] < num_arry[left_index]:
        root_index = left_index
    if right_index < length and num_arry[root_index] < num_arry[right_index]:
        root_index = right_index
    if root_index != i:
        num_arry[i],num_arry[root_index] = num_arry[root_index],num_arry[i]
        heapify(num_arry,length,root_index)

 

def heap_sort (num_arry):
    length = len(num_arry)
    for i in range (length//2-1,-1,-1):
        heapify(num_arry,length,i)
    for i in range(length-1,0,-1):
        num_arry[i],num_arry[0] = num_arry[0],num_arry[i]
        heapify(num_arry,i,0)
    return num_arry
 
print(selection_sort([77,71,26,20,0,12,57,24,23,48,1,25,56,98,63,50,28,39,96]))
print(quick_sort([77,71,26,20,0,12,57,24,23,48,1,25,56,98,63,50,28,39,96]))
print(insertion_sort([77,71,26,20,0,12,57,24,23,48,1,25,56,98,63,50,28,39,96]))
print(bubble_sort([77,71,26,20,0,12,57,24,23,48,1,25,56,98,63,50,28,39,96]))
print(heap_sort([77,71,26,20,0,12,57,24,23,48,1,25,56,98,63,50,28,39,96]))            