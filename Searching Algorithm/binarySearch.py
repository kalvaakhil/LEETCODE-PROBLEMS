def binarySearch(l,low,high,key):
    if(low<=high):
        mid=(low+high)//2
        if(l[mid]==key):
            return mid
        elif(l[mid]>key):
            return binarySearch(l,low,mid-1,key)
        elif(l[mid]<key):
            return binarySearch(l,mid+1,high,key)
    else:
        return -1
c=binarySearch(l,0,len(l)-1,3)
if(c!=-1):
    print("Element found at index pos",c)
else:
    print("Element not present in the array")
