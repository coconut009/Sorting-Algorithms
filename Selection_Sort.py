def selection_sort(num_str):
    length = len(num_str)-1

    for i in range (length):
        min_value_index =i

        for j in range (i+1, length+1):
            if num_str[j] < num_str[min_value_index]:
                min_value_index = j

        if min_value_index != i:
                num_str[min_value_index], num_str[i] = num_str[i], num_str[min_value_index]
    
    return num_str



