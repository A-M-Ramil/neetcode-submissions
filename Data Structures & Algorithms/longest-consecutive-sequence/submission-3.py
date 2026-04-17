class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums=set(nums)
        nums=list(nums)
        nums.sort()
        a=nums[0]
        c=1
        final=[]
        for i in range(1,len(nums)):
            
            if nums[i]==(a+1):
                c+=1
                a=nums[i]
            if nums[i]>(a+1):
                final.append(c)
                c=1
                a=nums[i]
        final.append(c)

        return max(final)