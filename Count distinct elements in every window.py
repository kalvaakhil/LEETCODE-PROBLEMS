#https://practice.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1?page=3&curated[]=1&sortBy=submissions
import collections
from collections import defaultdict
class Solution:
    def countDistinct(self,A,N,K):
        out = []
        dict1 = defaultdict(int)
        for i in range(K):
            dict1[A[i]] +=1
        l = len(dict1)
        out.append(l)
        for i in range(K,N):
            if A[i] != A[i-k]:
                dict1[A[i]] +=1
                dict1[A[i-K]] -=1
                if (dict1[A[i]] == 1 and dict1[A[i-K]] !=0):
                    l = l+1
                elif (dict1[A[i]] > 1 and dict1[A[i-k]] ==0):
                    l = l-1
            out.append(l)
        return out
