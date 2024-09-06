def MergeSort(list,l,r):
    if l<r:
        mid = (l+r)//2
        MergeSort(list,l,mid)
        MergeSort(list,mid+1,r)
        merge(list,l,r,mid)
        
def merge(list,l,r,mid):
    n1= mid-l+1
    n2= r-mid
    left =[0] * (n1)
    right = [0] * (n2)
    for x in range(0,n1):
        left[x] =  list[l+x]
    for x in range(0,n2):
        right[x] =   list[mid+1+x]
    
    i=0
    j=0
    k= l
    while i<n1 and j<n2:
        if left[i]<= right[j]:
            list[k] =left[i]
            i += 1
        else:
            list[k] =right[j]
            j += 1
        k +=1
    
    while i<n1:
        list[k] =left[i]
        i += 1
        k+=1
    
    while j<n2:
        list[k] =right[j]
        j += 1
        k +=1
    
list = [10,82,12,4,36,9,2,7,40,20]
print("Original List: " + " ".join(str(x) for x in list))
MergeSort(list,0,len(list)-1)
print("After Sorting: "+ " ".join(str(x) for x in list))