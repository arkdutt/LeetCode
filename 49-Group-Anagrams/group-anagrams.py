class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anag_dict[key].append(s)
        return anag_dict.values()