class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        res=[]
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values()) 