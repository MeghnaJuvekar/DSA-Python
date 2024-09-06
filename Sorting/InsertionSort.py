def InsertionSort(list):
    for i in range(1,len(list)):
        key = list[i]
        j = i-1
        while list[j]>key and j>=0:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
        # print(" ".join(str(x) for x in list))   

list = [10,82,12,4,36,9,2,7,40,20]
print("Original List: " + " ".join(str(x) for x in list))
InsertionSort(list)
print("After Sorting: "+ " ".join(str(x) for x in list))