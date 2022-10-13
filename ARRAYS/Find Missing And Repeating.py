#https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1?page=2&difficulty[]=1&sortBy=submissions
class Solution:
    def findTwoElement( self,arr, n):
        hash={}
        for i in arr:
            if i not in hash:
                hash[i]=1
            else:
                idx=i
        missing  = sum(range(n+1))-sum(set(arr))
        return idx,missing
                
