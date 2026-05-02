class Solution:
    def maxArea(self, heights: List[int]) -> int:
        final=0
        n=len(heights)
        l=0
        r=n-1
        # for i in range(n):
        #     l=i
        #     r=n-1
        #     while r>l:
        #         temp= (r-l)* min(heights[l],heights[r])
        #         if temp>final:
        #             final=temp
        #         r-=1
        # return final

        while l<r:
            h=min(heights[l],heights[r])
            temp=(r-l)*h
            if temp>final:
                final=temp
            if heights[l]>heights[r]:
                r-=1
            elif heights[l]<=heights[r]:
                l+=1
        return final
            










            
            
        