#https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1?page=1&curated[]=1&sortBy=submissions
class Solution:
    def longestCommonPrefix(self,a,n):
        size = len(a)
        if (size == 0):
            return ""
        if (size == 1):
            return a[0]
        a.sort()
        end = min(len(a[0]), len(a[size - 1]))
        i = 0
        while (i < end and
               a[0][i] == a[size - 1][i]):
            i += 1
        pre = a[0][0: i]
        return pre if len(pre)>=1 else -1
