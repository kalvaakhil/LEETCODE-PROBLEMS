class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        retv = []
        def backtrack(i, stack):
            if len(stack) >= 2:
                retv.append(stack)
            appear = set()
            for j in range(i, length):
                if nums[j] not in appear:
                    appear.add(nums[j])
                    if not stack or nums[j] >= stack[-1]:
                        backtrack(j+1, stack + [nums[j]])
        backtrack(0, [])
        return retv
        
