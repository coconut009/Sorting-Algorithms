def insertion_sort(num_str):
    length =range(1,len(num_str)) 
    for i in  length:
        value_to_sort = num_str[i]

        while num_str[i-1] > value_to_sort and i>0:
            num_str[i], num_str[i-1] = num_str[i-1], num_str[i]
            i=i-1
    return num_str

