# quick sort better named pivot sort:
# uses 2 functions main recursive one lets call it quick sort and a second one to comapre and swap values inplace call partition.



def quicksort (list ,low = 0, high = None ):
    
    if high == None:
        high = len(list)-1

    if high>low:
        pivot = partition(list,low,high)

        quicksort(list,low,pivot-1)
        quicksort(list,pivot+1,high)
    return list

        



def partition (list ,i, j):
    temp = i
    pivot = list[i]
    i+=1

    while j>i:
        while pivot>list[i]:
            i+=1
        while pivot<list[j]:
            j-=1
        list[i], list[j] = list[j], list[i]
    list[i], list[j] = list[j], list[i]

    list[j],list[temp] = list[temp], list[j]
    return j





list = [ 26, 181, 102, 125, 5, 82, 94, 145, 9, 151, 74, 184, 47, 132, 59, 183, 13, 178, 144, 98, 55, 27, 63, 123, 112, 2, 162, 190, 76, 142, 175, 34, 122, 72, 92, 100, 113, 101, 88, 58, 80, 21, 141, 25, 157, 42, 62]
print(quicksort(list))

