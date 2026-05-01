class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i1=0
        # i2=0
        # p=0
        # for i in range(len(numbers)):
        #     p=target-numbers[i]
        #     if p!=numbers[i]:
        #         if p in numbers:
        #             p1=i+1
        #             p2=numbers.index(p)+1

        #             return [p1,p2]

        l=0
        r=len(numbers)-1

        while l<r:
            total=numbers[l]+numbers[r]
            if total>target:
                r-=1
            elif total<target:
                l+=1
            
            else:
                return [l+1,r+1]
        
        return []
        
        