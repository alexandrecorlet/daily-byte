from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stackS = deque()
        stackT = deque()

        for c in s:
            if c == "#":
                if stackS:
                    stackS.pop()
                continue
            stackS.append(c)
        
        for c in t:
            if c == "#":
                if stackT:
                    stackT.pop()
                continue
            stackT.append(c)
        
        print(stackS)
        print(stackT)
        if len(stackT) != len(stackS):
            return False
        
        while stackT and stackS:
            x = stackT.pop()
            y = stackS.pop()
            if x != y:
                return False
        
        return True
