from collections import deque


class Solution:

    def isValid(self, s: str) -> bool:
        def match(c1: str, c2: str) -> bool:
            lsts = [
                ["(", ")"],
                ["[", "]"],
                ["{", "}"]
            ]
            return any(c1 in lst and c2 in lst for lst in lsts)
        
        stack = deque()
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
                continue
            if len(stack) == 0 or not match(c, stack[-1]):
                return False
            stack.pop()                
            
        return len(stack) == 0

