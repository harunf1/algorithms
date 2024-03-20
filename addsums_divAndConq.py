def addsums(array):
    if array == []:
        return 0
    return array[0] + addsums(array[1:])

def addsums_norm(list):

    total = 0

    for i in range(0, len(list)):
        total+= list[i]
    return total



def findmax(list):
    max = 0
    for i in range(0 ,len(list)):
        if max < list[i]:
            max = list[i]
        
    return max



def rcursive_max(list):
    


nums = [1,2,3,4,5]
print("standard addsums", addsums_norm(nums))
print("recursive divide and conquer :", addsums(nums))


print("finding max standard:", findmax(nums))