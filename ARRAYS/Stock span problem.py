#https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1?page=2&curated[]=1&sortBy=submissions
class Solution: 
    def calculateSpan(self,a,n):
        ans=[1]
        s=[[a[0],1]]
        for i in range(1,n):
            s1=s[-1]
            s2=s1[0]
            c=1
            while s and s2<=a[i]:
                p=s.pop()
                c=c+p[1]
                if s:
                    s1=s[-1]
                    s2=s1[0]
            ans.append(c)
            s.append([a[i],c])
        return ans
