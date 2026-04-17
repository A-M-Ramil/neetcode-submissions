class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=dict()
        for i in nums:
            if i not in s:
                s[i]=nums.count(i)
                
        print(s)
        s=dict(sorted(s.items(), key=lambda item: item[1], reverse=True))
        final=[]
        pa=list(s.keys())
        for i in range(k):
            final.append(pa[i])
            
        return final
        