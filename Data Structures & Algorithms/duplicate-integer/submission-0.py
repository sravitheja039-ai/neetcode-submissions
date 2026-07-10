class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h={}
        for i in nums:
            if i in h.keys():
                h[i]+=1
            else:
                h[i]=1
        for i in nums:
            if h[i]!=1:
                return True
        return False