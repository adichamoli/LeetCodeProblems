'''18 / 18 test cases passed.                        Status: Accepted
Runtime: 36 ms                                       Memory Usage: 14.2 MB'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def recur(k,n,buff,si):
            #print (output)
            if len(buff)==k and sum(buff)==n:
                #print (output)
                output.append(buff[:])
                return
            if len(buff)>=k:
                return
            if sum(buff)>n:
                return
            
            for i in range(si+1,10):
                if i in buff:
                    continue
                buff.append(i)
                recur(k,n,buff,i)
                buff.pop()
        
        output=[]
        recur(k,n,[],0)
        return (output)