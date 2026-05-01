class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1=0
        i2=0
        p=0
        for i in range(len(numbers)):
            p=target-numbers[i]
            if p!=numbers[i]:
                if p in numbers:
                    p1=i+1
                    p2=numbers.index(p)+1

                    return [p1,p2]
        
        