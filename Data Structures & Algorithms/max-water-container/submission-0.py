class Solution:
    def maxArea(self, heights: List[int]) -> int:
        final=0
        n=len(heights)
        for i in range(n):
            l=i
            r=n-1
            while r>l:
                temp= (r-l)* min(heights[l],heights[r])
                if temp>final:
                    final=temp
                r-=1
        return final


            
            
        