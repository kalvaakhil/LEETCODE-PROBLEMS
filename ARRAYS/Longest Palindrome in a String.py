#https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1?page=1&difficulty[]=1&category[]=Strings&sortBy=submissions
class Solution:
    def longestPalin(self, S):
        fi = fj = 0
        n = len(S)
        for i in range(n):
            j = i - 1
            k = i + 1
            while j >= 0 and k < n:
                if S[j] != S[k]:
                    break
                j -= 1
                k += 1
            if k-j-1 > fj-fi+1:
                fi = j + 1
                fj = k - 1
            if i < n-1 and S[i] == S[i+1]:
                j = i - 1
                k = i + 2
                while j >= 0 and k < n:
                    if S[j] != S[k]:
                        break
                    j -= 1
                    k += 1
                if k-j-1 > fj-fi+1:
                    fi = j + 1
                    fj = k - 1
        return S[fi:fj+1]
