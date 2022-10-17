#https://practice.geeksforgeeks.org/problems/31272eef104840f7430ad9fd1d43b434a4b9596b/1?page=1&status[]=unsolved&category[]=Strings&curated[]=1&sortBy=submissions
class Solution:
    def search(self, pat, s):
        ans = []
        i = 0
        n = len(pat)
        m = len(s)
        j = m-(n-1)
        while i <= j:
            if s[i:i+n] == pat:
                ans.append(i+1)
            i += 1
        return ans if len(ans) > 0 else [-1]
