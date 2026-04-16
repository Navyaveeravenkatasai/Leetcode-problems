class Solution:
    def largestInteger(self, num: int) -> int:
        even=[]
        odd=[]
        num=list(str(num))
        n=len(num)
        for i in num:
            if int(i) % 2 == 0:
                even.append(int(i))
            else:
                odd.append(int(i))
        even.sort(reverse=True)
        odd.sort(reverse=True)

        i = 0  # even index
        j = 0  # odd index
        
        result = []
        
        for d in num:
            if int(d) % 2 == 0:
                result.append(str(even[i]))
                i += 1
            else:
                result.append(str(odd[j]))
                j += 1
        
        return int("".join(result))