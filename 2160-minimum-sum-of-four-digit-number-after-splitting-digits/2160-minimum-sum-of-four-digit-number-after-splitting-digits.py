class Solution:
    def minimumSum(self, num: int) -> int:
        num =list(str(num))
        num.sort()
        new1=[]
        new2=[]
        for ch in range(0,len(num),2):
            new1.append(num[ch])
        new1=int(''.join(new1))
        for ch in range(1,len(num),2):
            new2.append(num[ch])
        new2=int(''.join(new2))
        total=new1+new2
        return total



