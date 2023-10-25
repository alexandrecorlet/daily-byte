# Given two strings s and t return whether or not s is an anagram of t.
# Note 1: An anagram is a word formed by reordering the letters of another word.
# Note 2: This program is not case sensitive (since it was not specified in the question)


# Time complexity: O(n + m) | Space complexity: O(m)
# where n is the size of the string s and m is the size of the string t 
def valid_anagram(s = "", t = ""):
    if len(s) != len(t):
        return False

    seen = set(t.lower())
    for char in s:
        if char.lower() not in seen:
            return False

    return True


def main():
    # Test cases:
    assert valid_anagram(s = "cat", t = "tac")
    assert valid_anagram(s = "Abba", t = "Bbaa")
    assert valid_anagram(s = "listen", t = "silent")
    assert not valid_anagram(s = "program", t = "function")
    print("OK: passed all test cases!")


if __name__ == "__main__":
    main()

