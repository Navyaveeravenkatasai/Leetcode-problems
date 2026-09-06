class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        for ch in range(len(events)):
            if counter == 10:
                break
            elif events[ch] == "W":
                counter += 1
            elif events[ch] == "WD" or events[ch] == "NB":
                score += 1
            else:
                score += int(events[ch])

        return [score,counter]
