class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        l=0
        r=1
        while r<len(prices):
            temp=prices[r]-prices[l]
            if temp>prof:
                prof=temp
            if prices[l] > prices[r]:
                l+=1
                r=l+1
            else:
                r+=1
        return prof
        