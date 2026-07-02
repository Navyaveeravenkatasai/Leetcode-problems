class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]

        for ch in range(1,n+1):
            if ch % 3 == 0 and ch % 5 == 0:
                res.append('FizzBuzz')
            elif ch % 5 == 0:
                res.append('Buzz')
            elif ch % 3 == 0:
                res.append('Fizz')
            else:
                res.append(str(ch))
        return res