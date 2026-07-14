class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h={}
        large=0
        ans=0
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for key,values in h.items():    
            if values>len(nums)//2:
                return key
        