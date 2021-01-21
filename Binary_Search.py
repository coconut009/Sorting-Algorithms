def binary_search(num_arry,target):
    start_index = 0
    end_index = len(num_arry)-1

    while start_index <= end_index:
        # use floor division => "//"
        midpoint = start_index+ (end_index-start_index)//2
        midpoint_value = num_arry[midpoint]

        if midpoint_value == target:
            return midpoint
        
        elif target<midpoint_value:
            end_index = midpoint - 1

        else:
            start_index = midpoint+1
    
    return None

num_arry = [0, 1, 12, 20, 23, 24, 25, 26, 28, 39, 48, 50, 56, 57, 63, 71, 77, 96, 98]
target = 26

print(binary_search(num_arry,target))