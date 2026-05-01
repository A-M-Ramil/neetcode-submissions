class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=0
        r=len(s)-1
        while l<r:
            p1=ord(s[l])
            p2=ord(s[r])
            if s[l]==' ' or p1<48 or  57<p1<97 or p1>122:#48 to 57 97 to 122
                l+=1
                continue
            elif s[r]==' ' or p2<48 or  57<p2<97 or p2>122:
                r-=1
                continue
            
            elif s[r]!=s[l]:
                return False
            
            l+=1
            r-=1

        return True
            
