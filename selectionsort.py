def selection_sort_asc(list):
    for i in range(len(list)):
        min = i 
        for j in range (i, len(list)):
            if list[j] < list[min]:
               min = j
        list[i], list[min] = list[min], list[i]
    return list


list = [1,7,6,5,9,3,12,56,43,23,77,56,44,12,9,5,3,5]
print(selection_sort_asc(list))

