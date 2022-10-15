#https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1?page=1&difficulty[]=1&category[]=Strings&sortBy=submissions
class Solution:
    def longestUniqueSubsttr(self, S):
        d = {}
        ans = 0
        s = 0
        for i in range(len(S)):
            if S[i] in d:
                s = max(s, d[S[i]]+1)
            d[S[i]] = i
            ans = max(ans, i-s+1)
        return ans
