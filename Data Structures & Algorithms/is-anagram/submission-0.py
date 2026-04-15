class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s=len(s)
        len_t=len(t)
        if len_s!=len_t:
            return False
        else:
            if len_s==0:
                return True
            s=sorted(s)
            t=sorted(t)
            for i in range(len_s):
                if s[i]!=t[i]:
                    return False
            
            return True