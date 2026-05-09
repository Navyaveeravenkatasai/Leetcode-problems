class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        res=[]
        
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                break
        num = int(''.join(num))
        return num