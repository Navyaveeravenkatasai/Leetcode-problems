class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
            q = deque()

            for i in range(len(tickets)):
                q.append((tickets[i], i))

            time = 0

            while q:

                ticket, index = q.popleft()

                ticket -= 1
                time += 1

                if ticket == 0 and index == k:
                    return time

                if ticket > 0:
                    q.append((ticket, index))
