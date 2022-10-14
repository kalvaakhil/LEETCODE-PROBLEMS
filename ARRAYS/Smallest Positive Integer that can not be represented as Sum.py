#https://practice.geeksforgeeks.org/problems/b6b608d4eb1c45f2b5cace77c4914f302ff0f80d/1?page=1&difficulty[]=2&sortBy=submissions
class Solution:
    def smallestpositive(self, a, n):
        a.sort()
        res=1
        for i in range(0,n ):
            if(a[i]<=res):
                res=res+a[i]
        return res
