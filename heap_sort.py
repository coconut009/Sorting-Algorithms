#build the binary tree
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
 
 
    