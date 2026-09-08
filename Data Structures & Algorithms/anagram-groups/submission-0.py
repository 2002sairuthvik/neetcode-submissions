class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = defaultdict(list)

        for s in strs:
            sorted_key = ''.join(sorted(s))
            c[sorted_key].append(s)

        return list(c.values())