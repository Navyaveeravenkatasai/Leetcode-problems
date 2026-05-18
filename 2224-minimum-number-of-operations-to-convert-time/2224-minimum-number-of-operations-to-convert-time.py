class Solution:
    def convertTime(self, current: str, correct: str) -> int:

        curr_hours, curr_minutes = map(int, current.split(":"))
        current_total = curr_hours * 60 + curr_minutes

        corr_hours, corr_minutes = map(int, correct.split(":"))
        correct_total = corr_hours * 60 + corr_minutes

        diff = correct_total - current_total

        operations = 0

        times = [60, 15, 5, 1]

        for t in times:
            operations += diff // t
            diff %= t

        return operations