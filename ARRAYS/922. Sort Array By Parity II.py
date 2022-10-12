class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[i for i in nums if i%2==0]
        odd=[i for i in nums if i%2!=0]
        res=[]
        for i in range(len(nums)//2):
            res.append(even[i])
            res.append(odd[i])
        return res
