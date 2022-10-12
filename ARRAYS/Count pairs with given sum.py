#https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1?page=1&category[]=Arrays&sortBy=submissions
class Solution:
    def getPairsCount(self, a, n, k):
        d={}
        c=0
        for i in range(n):
            if k-a[i] in d:
                c+=d[k-a[i]]
            if(a[i] in d):
                d[a[i]]+=1
            else:
                d[a[i]]=1
        return c
