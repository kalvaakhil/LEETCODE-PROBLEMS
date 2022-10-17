#https://practice.geeksforgeeks.org/problems/replace-every-element-with-the-least-greater-element-on-its-right/1
# from typing import List
# class Solution:
#     def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
#         c=0
#         l=[]
#         for i in range(n):
#             mx=arr[i]
#             x=arr[i+1:]
#             x.sort()
#             for j in range(0,len(x)):
#                 if(mx<x[j]):
#                     mx=x[j]
#                     l.append(mx)
#                     break
#             else:
#                 l.append(-1)
#         return l gives tle below is optimal solution
from typing import List
import bisect
from bisect import *
class Solution:
        def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
            s_arr, ans = [], [0]*n
            for i in range(n-1, -1, -1):
                idx = bisect_right(s_arr, arr[i])
                if idx < len(s_arr):
                    ans[i] = s_arr[idx]
                else:
                    ans[i] = -1
                s_arr.insert(idx, arr[i])
            return ans
