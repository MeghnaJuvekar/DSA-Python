# Iterative approach
def LinearSearch(list,target):
    for index in range(0,len(list)):
        if list[index] == target:
            return f"Linear: Target is at index {index}"
    return "Target not found."

# Recursive approach
def LinearSearchRecursive(list,target,index=0):
    # if index reaches the end of the list
    if index == len(list):
        return "Target not found."
    
    # if element is found
    if list[index] == target:
        return f"Recursive: Target is at index {index}"
    return LinearSearchRecursive(list,target,index+1)
    
list = [10,82,12,4,36,9,2,7,40,20]
target = 40
print(LinearSearch(list,target))
print(LinearSearchRecursive(list,target))