class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq = {}
        position = {}
        for i,num in enumerate(nums):
            freq[num] = freq.get(num,0) + 1

            if num not in position:
                position[num] = []

            position[num].append(i)
        
        count = 0

        for key,value in freq.items():
            if value == 3:
                indices = position[key]

                if indices[1] - indices[0] == indices[2] - indices[1]:
                    count += 1

        return count