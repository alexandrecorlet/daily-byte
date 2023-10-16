# Given a string, return whether or not it forms a palindrome 
# ignoring case and non-alphabetical characters.
# (c) alexandrecorlet

# Time complexity O(n) | Space complexity O(1)
# where n is the size of the string
def valid_palindrome(s):
    n = len(s)
    i, j = 0, n - 1
    while i <= j:
        while i < n and not s[i].isalpha():
            i += 1
        while j > 0 and not s[j].isalpha():
            j -= 1
        if i >= n  or j < 0 or s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def main():
    # Test cases
    assert valid_palindrome("level")
    assert not valid_palindrome("algorithm")
    assert valid_palindrome("A man, a plan, a canal: Panama.") 
    assert valid_palindrome("....a")
    assert valid_palindrome("....a.")
    assert valid_palindrome("a")
    assert not valid_palindrome("...")
    print("OK passed all tests!")


if __name__ == "__main__":
    main()

