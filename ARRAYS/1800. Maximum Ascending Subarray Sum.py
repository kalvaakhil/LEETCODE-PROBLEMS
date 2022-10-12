#https://leetcode.com/problems/maximum-ascending-subarray-sum/
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        s=0
        for i in range(0,len(nums)):
            if i==0 or nums[i - 1] < nums[i]:
                s+= nums[i]
            else:
                s = nums[i]
            res = max(res, s)
        return res
