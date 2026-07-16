class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        i=0
        j=len(num)-1
        while i<j:
            current=num[i]+num[j]
            if current==target:
                return [i+1,j+1]
            elif current<target:
                i+=1
            else:
                j-=1
        