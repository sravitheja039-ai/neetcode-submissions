class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        ans=[]
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        arr=[]
        for key,values in h.items():
            arr.append((values,key))
        arr.sort(reverse=True)
        ans=[]
        for i in range(k):
            ans.append(arr[i][1])
        return ans

            
        