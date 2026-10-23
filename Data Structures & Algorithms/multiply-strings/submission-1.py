class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        
        m,n = len(num1),len(num2)
        res=[0]*(m+n)
        num1,num2=num1[::-1],num2[::-1]
        for i1 in range(m):
            for i2 in range(n):
                digit=int(num1[i1])*int(num2[i2])
                res[i1+i2]+=digit
                res[i1+i2+1]+=res[i1+i2]//10
                res[i1+i2] = res[i1+i2]%10
        res,beg=res[::-1],0
        while beg<len(res) and res[beg]==0:
            beg+=1
        res=map(str,res[beg:])
        return "".join(res)