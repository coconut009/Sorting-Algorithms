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

