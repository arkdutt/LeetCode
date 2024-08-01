class Solution:
    def romanToInt(self, s: str) -> int:

        hm = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        ans = 0

        for i in range(len(s)):

            if i < len(s)-1 and hm[s[i]] < hm[s[i+1]]:
                ans -= hm[s[i]]
            else:
                ans += hm[s[i]]
        return ans
            
