class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        final=0
        temp=0
        tempe=''
        while r<len(s):
            if s[r] in tempe:
                if temp>final:
                    final=temp
                tempe=''
                temp=0
                l+=1
                r=l
            tempe=tempe+s[r]
            r+=1
            temp+=1
        if temp>final:
            final=temp
        return final

