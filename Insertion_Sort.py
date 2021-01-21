def insertion_sort(num_arry):
    length =range(1,len(num_arry)) 
    for i in  length:
        value_to_sort = num_arry[i]

        while num_arry[i-1] > value_to_sort and i>0:
            num_arry[i], num_arry[i-1] = num_arry[i-1], num_arry[i]
            i=i-1
    return num_arry

