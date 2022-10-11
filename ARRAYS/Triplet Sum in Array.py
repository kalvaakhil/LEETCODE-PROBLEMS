#https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1?page=1&category[]=Sorting&sortBy=submissions
class Solution:
    def find3Numbers(self,a,n,x):
        a.sort()
        for i in range(n):
            y=x-a[i]
            j=i+1
            k=n-1
            while j<k:
                c=a[j]+a[k]
                if(c==y):
                    return 1
                elif(c>y):
                    k-=1
                elif(c<y):
                    j+=1
        return 0
