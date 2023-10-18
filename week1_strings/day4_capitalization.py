# Given a string, return whether or not it uses capitalization correctly. 
# A string correctly uses capitalization if all letters are capitalized, 
# no letters are capitalized, or only the first letter is capitalized.

"""
# Time Complexity: O(n) | Space Complexity: O(n)
# where n is the size of the string
def valid_capitalization(s):
    return s == s.title() or s == s.lower() or s == s.upper()
"""

# Time compleixty: O(n) | Space complexity: O(1)
# where n is the size of the string
def valid_capitalization(s):
    """
    Given a string s, this function checks if s
    is has a valid capitalization.
    """
    num_upper = 0
    for c in s:
        if c.isupper():
            num_upper += 1

    if num_upper == len(s) or num_upper == 0:
        # all characters are either uppercase or lowercase 
        return True
    elif num_upper == 1 and s[0].isupper():
        # Only the first character is uppercase
        return True

    return False
    # return num_upper == len(s) or (num_upper == 1 and s[0].isupper()) or num_upper == 0


def main():
    # Test cases:
    assert valid_capitalization("USA")
    assert valid_capitalization("Calvin")
    assert not valid_capitalization("compUter")
    assert not valid_capitalization("COMPuTER")
    assert not valid_capitalization("COMPUter")
    assert valid_capitalization("coding")
    assert valid_capitalization("")     # Assuming an empty string is a valid capitalization
    print("OK: passed all tests!")


if __name__ == "__main__":
    main()

