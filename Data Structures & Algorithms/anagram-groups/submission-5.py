class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wa=[]
        for i in strs:
            if i!='':
                s=[i]
                s.append(sorted(list(i)))
                wa.append(s)
            else:
                s=[i]
                s.append([''])
                wa.append(s)
                
        print(wa)
        wa.sort(key=lambda x: x[1])

        ss=[wa[0][0]]
        p=wa[0][1]
        final=[]
        for i in range(1, len(strs)):
            if wa[i][1]==p:
                ss.append(wa[i][0])
            elif wa[i][1]!=p:
                final.append(ss)
                ss=[]
                ss.append(wa[i][0])
                p=wa[i][1]

        final.append(ss)
        return final
    