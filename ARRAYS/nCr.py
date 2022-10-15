#https://practice.geeksforgeeks.org/problems/ncr1019/1?page=2&difficulty[]=1&status[]=unsolved&sortBy=submissions
class Solution:
    def nCr(self, n, r):
        if n<r:
            return 0
        else:
            p1=1
            p2=1
            p3=1
            for i in range(1,n+1):
                p1*=i
                if i==r:
                    p2=p1
                if i==n-r:
                    p3=p1
            return p1//(p2*p3)%1000000007
