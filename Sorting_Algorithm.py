def selection_sort(num_str):
    length = len(num_str)

    for i in range (length):
        min_value_index =i

        for j in range (i, length):
            if num_str[j] < num_str[min_value_index]:
                min_value_index = j

        if min_value_index != i:
                num_str[min_value_index], num_str[i] = num_str[i], num_str[min_value_index]
    
    return num_str

def quick_sort(num_str):
    length = len(num_str)
    if length <=1:
        return num_str
    else:
        pivot = num_str.pop()

    
    items_greater = []
    items_lower = []

    for item in num_str:
        if item > pivot:
            items_greater.append(item)
        
        else:
            items_lower.append(item)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


def insertion_sort(num_str):
    length =range(1,len(num_str)) 
    for i in  length:
        value_to_sort = num_str[i]

        while num_str[i-1] > value_to_sort and i>0:
            num_str[i], num_str[i-1] = num_str[i-1], num_str[i]
            i=i-1
    return num_str

def bubble_sort(num_str):
    length = len(num_str)
    value_sorted = False

    while not value_sorted:
        value_sorted = True
        for i in range (length-1):
            if  num_str[i] > num_str[i+1]:
                value_sorted = False
                num_str[i],num_str[i+1] = num_str[i+1],num_str[i]
    return num_str

print(selection_sort([77,71,26,20,0,12,57,24,23,48,1,25,56,98,63,50,28,39,96]))
print(quick_sort([77,71,26,20,0,12,57,24,23,48,1,25,56,98,63,50,28,39,96]))
print(insertion_sort([77,71,26,20,0,12,57,24,23,48,1,25,56,98,63,50,28,39,96]))
print(bubble_sort([77,71,26,20,0,12,57,24,23,48,1,25,56,98,63,50,28,39,96]))
            