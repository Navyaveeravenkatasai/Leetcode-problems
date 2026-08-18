class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        res = []
        left = 0
        right = k - 1

        freq = {}

        while right < len(nums):
            seen = set()

            for i in range(left, right + 1):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    freq[nums[i]] = freq.get(nums[i], 0) + 1
            left += 1
            right += 1

        for ch in freq:
            if freq[ch] == 1:
                res.append(ch)

        if len(res) == 0:
            return -1

        return max(res)