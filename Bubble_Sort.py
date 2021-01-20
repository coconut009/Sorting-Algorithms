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

