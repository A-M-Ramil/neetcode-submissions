class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            flag1=self.counters(i)
            if flag1==False:
                return False
        
        
        c=0
        rows=[]
        while c!=9:
            ss=[]
            for i in range(9):
                ss.append(board[i][c])
            rows.append(ss)
            c+=1
            
                
        for i in rows:
            flag1=self.counters(i)
            print(flag1)
            if flag1!=True:
                return False
        
        
        
        
        
        
        
        
        
        
        
        d=dict()
        t=0
        while t!=3:
            d[0]=[]
            d[1]=[]
            d[2]=[]
            
            for i in range(3):
                p=board.pop(0)
                a=p[:3]
                b=p[3:6]
                c=p[6:9]
                
                d[0].extend(a)
                d[1].extend(b)
                d[2].extend(c)
            t+=1
            for i,j in d.items():
                pp=self.counters(j)
                if pp==False:
                    return False
        return True


    def counters(self, a):
        for i in a:
            if i!='.':
                if a.count(i)>1:
                    return False
                    
        return True