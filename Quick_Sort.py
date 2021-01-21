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

