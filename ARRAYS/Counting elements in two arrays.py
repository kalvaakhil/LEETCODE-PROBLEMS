#https://practice.geeksforgeeks.org/problems/counting-elements-in-two-arrays/1?page=2&difficulty[]=1&category[]=Arrays&sortBy=submissions
#User function Template for python3
from bisect import bisect_right
class Solution:
      def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        arr2.sort()
        result=[]
        for i in arr1:
            ind = bisect_right(arr2,i)
            result.append(ind)
        return result
      #tle one below
      
class Solution:
      def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        def bin(arr,n,x):
            si=0
            ei=n-1
            while si<=ei:
                mid=si+(ei-si)//2
                if arr[mid]<=x:
                    si=mid+1
                else:
                    ei=mid-1
            return ei
        arr2.sort()
        ans=[]
        for i in range(n1):
            pos=bin(arr2,n2,arr1[i])
            ans.append(pos+1)
        return ans    
    
