class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq={}

        for ch in nums:
            freq[ch] = freq.get(ch,0) + 1

        for value in freq.values():
            if value < 2:
                continue
            
            prime = True


            for i in range(2, int(value ** 0.5) + 1):
                if value % i == 0:
                    prime = False
                    break

            if prime:
                return True
        return False