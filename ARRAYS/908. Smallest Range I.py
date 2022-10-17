class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mx=max(nums)
        mi=min(nums)
        if mi+ k >= mx - k:
            return 0
        else:
            return (mx - k) - (mi + k)
 
