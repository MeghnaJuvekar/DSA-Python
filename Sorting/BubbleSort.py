# Compare adjacent and Swap if left > right
def BubbleSort(list):
    for i in range(0, len(list)-1):
        for j in range(0,len(list)-i-1):
            if list[j]>list[j+1]:
                list[j], list[j + 1] = list[j + 1], list[j]
        # print(" ".join(str(x) for x in list))    # print this to check list after each iteration

list = [10,82,12,4,36,9,2,7,40,20]
print("Original List: " + " ".join(str(x) for x in list))
BubbleSort(list)
print("After Sorting: "+ " ".join(str(x) for x in list))