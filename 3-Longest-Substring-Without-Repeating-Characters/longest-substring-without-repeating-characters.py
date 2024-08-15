class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #abcabcbb
        #l
        #r

        l = 0
        r = 0
        n = len(s)
        visited = set()
        longest = 0

        for r in range(n):

            while s[r] in visited:
                visited.remove(s[l])
                l+=1
            
            w = (r-l)+1
            longest = max(longest, w)
            visited.add(s[r])
        return longest