#https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1?page=5&difficulty[]=1&sortBy=submissions
from itertools import permutations
class Solution:
    def find_permutation(self, S):
        l=[]
        s=permutations(S,len(S))
        for i in s:
            c="".join(i)
            if c not in l:
                l.append(c)
        l.sort()
        return l
