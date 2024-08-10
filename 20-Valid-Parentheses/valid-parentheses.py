class Solution:
    def isValid(self, s: str) -> bool:

        hm = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for char in s:

            #if it is opening bracket -> push it to the stack
            if char not in hm:
                stack.append(char)
            
            #if it is a closing bracket
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hm[char]:
                        return False

        return True if not stack else False


        #Time Complexity: O(N)
        #Space Complexity: O(N)