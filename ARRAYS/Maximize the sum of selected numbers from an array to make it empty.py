#https://practice.geeksforgeeks.org/problems/maximize-the-sum-of-selected-numbers-from-an-array-to-make-it-empty0836/1
import collections
from collections import Counter
class Solution:
    def maximizeSum (self,arr, n) :
        d=dict(Counter(arr))
        s=0
        for i in range(n-1,-1,-1):
            x=arr[i]
            if(d[x]>=1):
                s+=x
                d[x]-=1
                if x-1 in d:
                    d[x-1]-=1
        return s
