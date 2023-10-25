# Given a string, return the index of its first unique character. If a unique character does not exist, return -1.
# (c) author: Alexandre Corlet


# Time complexity: O(n) | Space complexity: O(n)
# where n is the size of the string s
def first_unique_char(s):
    hist = _histogram(s)
    for i in range(len(s)):
        char = s[i]
        if hist[char] == 1:
            return i
    return -1


# Time complexity: O(n) | Space complexity: O(n)
# where n is the size of the string s
def _histogram(s):
    hist = dict()
    for c in s:
        hist[c] = hist.get(c, 0) + 1
    return hist


def main():
    # Test cases:
    assert first_unique_char("abcabd") == 2
    assert first_unique_char("thedailybyte") == 1
    assert first_unique_char("developer") == 0
    assert first_unique_char("aaaaaaa")
    assert first_unique_char("aab") == 2
    assert first_unique_char("") == -1
    print("OK: passed all test cases!")


if __name__ == "__main__":
    main()

