def QuickSort(list,low,high):
    if low<high:
        pivot = Partition(list,low,high)
        QuickSort(list,low,pivot-1)
        QuickSort(list,pivot+1,high)
    return -1

def Partition(list,low,high):
    pivot = list[high]
    i = low-1
    for j in range(low,high):
        if list[j] < pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[high] = list[high], list[i+1]
    return i+1
            
list = [10,82,12,4,36,9,2,7,40,20]
print("Original List: " + " ".join(str(x) for x in list))
QuickSort(list,0,len(list)-1)
print("After Sorting: "+ " ".join(str(x) for x in list))