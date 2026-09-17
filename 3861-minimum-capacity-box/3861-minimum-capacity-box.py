class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        mini = float('inf')
        index = -1
        for i in range(0,len(capacity)):
            if capacity[i] >= itemSize and capacity[i] < mini:
                mini = capacity[i]
                index = i
        return index