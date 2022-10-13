#https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1?page=2&difficulty[]=1&sortBy=submissions
class Solution:
    def missingNumber(self,a,n):
        if len(a) == 1 and a[0] != 1 or 1 not in a:
            return 1
        a = list(set(a))
        a.sort()
        s = a.index(1)
        a[:] = a[s:]
        for i in range(len(a)-1):
            if a[i] + 1 == a[i + 1]:
                continue
            else:
                return a[i] + 1
        return max(a) + 1
