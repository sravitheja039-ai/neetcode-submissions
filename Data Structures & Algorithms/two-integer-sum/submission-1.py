class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            compli=target-nums[i]
            if compli in h:

                 return [h[compli],i]
            h[nums[i]]=i
