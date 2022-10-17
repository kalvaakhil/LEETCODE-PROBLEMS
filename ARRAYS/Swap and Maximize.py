#https://practice.geeksforgeeks.org/problems/swap-and-maximize5859/1?page=1&status[]=unsolved&curated[]=7&sortBy=submissions
def maxSum(arr,n):
    # code here
    arr.sort()
    i=0
    x=1
    while x<n:
        new=arr.pop(-1)
        arr.insert(x,new)
        x=x+2
    c=0
    for i in range(n-1):
        c=c+abs(arr[i+1]-arr[i])
    c=c+abs(arr[-1]-arr[0])
    return c  
