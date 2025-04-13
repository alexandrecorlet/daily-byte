"""
This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true

Solution: to be a palindrome a string must satisfy the following property: s[0] == s[n], s[1] == s[n - 1], ..., s[i] == s[n - i]
this means that characters in corresponding positions must be equal. Just loop through the string and check if the property is valid,
however, be careful with non letter characters.
"""

# Time Complexity: O(n) | Space Complexity: O(1)
# where n is the length of the string s
def is_palindrome(s):
    """Given a string check if its a palindrome or not."""

    i, j = 0, len(s) - 1
    while i <= j:
        
        # Skip non letter characters (digits, whitespaces, etc.)
        while i <= j and not s[i].isalpha():
            i += 1
        while j >= i and not s[j].isalpha():
            j -= 1
        if i > j:
            return False
        # Compare corresponding characters in the string
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    
    return True


def main():
    s = input()
    print(is_palindrome(s))


if __name__ == "__main__":
    main()

