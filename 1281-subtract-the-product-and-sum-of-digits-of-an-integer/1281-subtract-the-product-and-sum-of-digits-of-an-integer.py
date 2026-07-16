class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        pro = 1
        temp = n
        while n > 0:
            pro *= n % 10
            n = n // 10

        while temp > 0:
            summ += temp % 10
            temp = temp // 10
        tot =  pro - summ
        return tot



