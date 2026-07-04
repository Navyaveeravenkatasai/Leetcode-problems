class Solution:
    def average(self, salary: List[int]) -> float:

        mini = min(salary)
        maxi = max(salary)

        salary.remove(mini)
        salary.remove(maxi)

        avg = sum(salary) / len(salary)

        return avg

