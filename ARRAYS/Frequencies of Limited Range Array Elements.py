#https://practice.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1?page=2&category[]=Arrays&sortBy=submissions
from collections import Counter
class Solution:
    def frequencyCount(self, arr, N, P):
        c=dict(Counter(arr))
        l=[]
        for i in range(1,N+1):
            if(i in c):
                l.append(c[i])
            else:
                l.append(0)
        arr[:]=l[:]
