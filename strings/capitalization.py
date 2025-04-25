"""
Given a string, return whether or not it uses capitalization correctly. 
A string correctly uses capitalization if all letters are capitalized, 
no letters are capitalized, or only the first letter is capitalized.

Examples:
"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""

# Time complexity: O(n) | Space Complexity: O(1)
# where n is the length of the string s
def is_correctly_capitalized(s: str) -> bool:
    
    if all(c.islower() for c in s):
        return True
    if all(c.isupper() for c in s):
        return True
    if s[0].isupper() and all(s[i].islower() for i in range(1, len(s))):
        return True

    return False


# note: using s == s.lower() or s == s.upper() or s == s.capitalize() works, but is O(n) space
# due to string immutability in Python.

def main():
    s = input()
    print(is_correctly_capitalized(s))


if __name__ == "__main__":
    main()

