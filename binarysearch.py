def binarysearch(list, target):
    
    low = 0 
    high = len(list)-1
    
    while low <= high:
        
        mid = (low + high)//2

        if list[mid] == target:
            return mid
        if list[mid] > target:
            high = mid-1
        else:
            low = mid+1


def recursive_binary_search(list,target,high = None,low = 0):

    if high is None:
        high = len(list)-1

    if low <= high:
        mid = (low + high)//2
    else:
        return None 

    if list[mid] == target:
        return mid
    elif list[mid] > target:
        return recursive_binary_search(list,target,mid-1,low = low)
    else:
        return recursive_binary_search(list,target, high=high , low = mid+1)



sorted_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
num = 26 
index = binarysearch(sorted_numbers, num)
if index == None:
    print("number dosnt exist in list ")    
else: 
    print("the index is ",index )



index2 = recursive_binary_search(sorted_numbers, num) 
if index2 == None:
    print("number dosnt exist in list (Recursive) ")    
else: 
    print("the index is (Recursive):    ",index2 )

# Ok im going to make a clearer version of this Binary search

