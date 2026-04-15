class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        nums=sorted(nums)
        p=nums[0]
        for i in nums[1:]:
            if i==p:
                return True
            p=i
        return False
        