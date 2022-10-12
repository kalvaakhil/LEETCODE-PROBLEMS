#https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1?page=2&category[]=Arrays&sortBy=submissions
class Solution:
	def rowWithMax1s(self,arr, n, m):
# 		res = -1
# 		maxOne = 0
# 		for i in range(n):
# 		    count = 0
# 		    for j in range(m):
# 		        if arr[i][j]==1:
# 		            count+=1
# 		    if count>maxOne:
# 		        maxOne = count
# 		        res= i
# 		return res
	    def binarysearch(arr,low,high):
	        if(low<=high):
	            mid=(low+high)//2
	            if(arr[mid]==1 and(mid==0 or arr[mid-1]==0)):
	                return mid
	            elif(arr[mid]==0):
	                return binarysearch(arr,mid+1,high)
	            else:
	                return binarysearch(arr,low,mid-1)
	        return -1
	    r=len(arr)
	    c=len(arr[0])
	    max_row_index=-1
	    mx=-1
	    for i in range(r):
	        ind=binarysearch(arr[i],0,c-1)
	        if(ind!=-1 and c-ind>mx):
	            mx=c-ind
	            max_row_index=i
	    return max_row_index
