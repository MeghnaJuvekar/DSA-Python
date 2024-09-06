# Considering min and placing it at the start
def SelectionSortMin(list):
    for i in range(0, len(list)-1):
        min = i
        for j in range(i,len(list)):
            if list[min]>list[j]:
                min = j
        list[min], list[i] = list[i], list[min]
        # print(" ".join(str(x) for x in list))    # print this to check list after each iteration

# Considering max and placing it at the end
def SelectionSortMax(list):
    for i in range(0, len(list)-1):
        max = 0
        for j in range(1,len(list)-i):
            if list[max]<list[j]:
                max = j
        list[max], list[j] = list[j], list[max]
        # print(" ".join(str(x) for x in list))    # print this to check list after each iteration

list = [10,82,12,4,36,9,2,7,40,20]
print("Original List: " + " ".join(str(x) for x in list))
SelectionSortMin(list)
print("Min : After Sorting: "+ " ".join(str(x) for x in list))
list = [10,82,12,4,36,9,2,7,40,20]
SelectionSortMax(list)
print("Max : After Sorting: "+ " ".join(str(x) for x in list))