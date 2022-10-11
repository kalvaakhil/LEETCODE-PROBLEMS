#https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1?page=3&curated[]=1&sortBy=submissions
class Solution:
    def findLongestConseqSubseq(self,nums, N):
        if(nums==[]):
            return 0
        nums=list(set(nums))
        nums.sort()
        c=0
        m=0
        for i in range(1,len(nums)):
            if(1+nums[i-1]==nums[i]):
                c+=1
            else:
                m=max(m,c+1)
                c=0
        c=max(m,c+1)
        return c
