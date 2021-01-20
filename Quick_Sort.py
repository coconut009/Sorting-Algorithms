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

