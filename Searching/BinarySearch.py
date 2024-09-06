# Iterative approach
def BinarySearch(list,target,start,end):
    while start<end:
        mid = int((start + end) /2)
        if list[mid]<target:
            start = mid+1           # Discard left and shift right 
        elif list[mid]>target:
            end = mid-1             # Discard right shift left
        else:
            return f"Binary: Target is at index {mid}" 
    return "Binary: Target not found."

# Recursive approach
def BinarySearchRecursive(list,target,start,end):
    
    if start<end:
        mid = int((start + end) /2)
        if list[mid]<target:
            return BinarySearchRecursive(list,target,mid+1,end)
        elif list[mid]>target:
            return BinarySearchRecursive(list,target,start,mid-1)
        else:
            return f"Recursive: Target is at index {mid}" 
    return "Recursive: Target not found."

list = [2,4,7,9,10,12,20,36,40,82]            # sorted list
target = 7
print(BinarySearch(list,target,0, len(list)-1))
print(BinarySearchRecursive(list,target,0, len(list)-1))