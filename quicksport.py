# quick sort better named pivot sort:
# uses 2 functions main recursive one lets call it quick sort and a second one to comapre and swap values inplace call partition.



def quicksort(list, low = 0, high = None):
    if high == None:
        high = len(list)

    if high>low:
        pivot = partition(list,low,high)
        quicksort(list,low,pivot+1)
        quicksort(list,pivot-1)


def partition(list, i , j):
    pivot = list[i]

    while pivot > list[i]:
        if 


