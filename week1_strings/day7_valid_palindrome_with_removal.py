# Given a string and the ability to delete at most one character, 
# return whether or not it can form a palindrome.
# Note: a palindrome is a sequence of characters that reads the 
# same forwards and backwards.


# Time Complexity: O(n) | Space Complexity: O(1)
# where n is the length of the string s
def valid_palindrome_with_removal(s):

    n = len(s)
    valid = removal = True 
    i, j = 0, n - 1
    while i <= j and valid:

        if s[i] != s[j]:
            if not removal:
                return False 
            removal = False
            if i+1 < n and s[i+1] == s[j]:
                i += 1
            elif j-1 >= 0 and s[j-1] == s[i]:
                j -= 1
            continue

        i += 1
        j -= 1

    return True
         

def main():
    # Test cases:
    assert valid_palindrome_with_removal("abcba")
    assert valid_palindrome_with_removal("foobof")
    assert not valid_palindrome_with_removal("abccab")
    assert valid_palindrome_with_removal("aaa")
    assert not valid_palindrome_with_removal("abc")
    assert valid_palindrome_with_removal("a")
    print("OK passed all test cases!")


if __name__ == "__main__":
    main()

