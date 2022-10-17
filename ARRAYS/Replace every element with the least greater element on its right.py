#https://practice.geeksforgeeks.org/problems/replace-every-element-with-the-least-greater-element-on-its-right/1
from typing import List
class Solution:
    def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
        c=0
        l=[]
        for i in range(n):
            mx=arr[i]
            x=arr[i+1:]
            x.sort()
            for j in range(0,len(x)):
                if(mx<x[j]):
                    mx=x[j]
                    l.append(mx)
                    break
            else:
                l.append(-1)
        return l
