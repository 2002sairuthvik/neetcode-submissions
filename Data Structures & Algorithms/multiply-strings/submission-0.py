class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        char_to_num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        num_to_char = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

        val1 = 0
        for n in num1:
            val1=val1*10+char_to_num[n]
        
        val2=0
        for n in num2:
            val2=val2*10+char_to_num[n]
        
        total= val1*val2
        res=""
        if total==0:
            return "0"
        else:
            while total:
                remainder=total%10
                res+=num_to_char[remainder]
                total = total//10
        return res[::-1]
