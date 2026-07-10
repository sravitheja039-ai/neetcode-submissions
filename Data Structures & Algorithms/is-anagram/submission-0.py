class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        v={}
        for i in s:
            if i in h.keys():
                h[i]+=1
            else:
                h[i]=1
        for i in t:
            if i in v.keys():
                v[i]+=1
            else:
                v[i]=1
        if h==v:
            return True
        return False
        