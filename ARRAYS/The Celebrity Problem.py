#https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1?page=2&difficulty[]=1&sortBy=submissions
class Solution:
    def celebrity(self, M, n):
        count=0
        for i in range(n):
            if 1 not in M[i]:
                count+=1
                ans=i
        if count==1:
            return ans
        return -1
