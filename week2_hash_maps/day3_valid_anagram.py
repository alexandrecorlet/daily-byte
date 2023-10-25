# Given two strings s and t return whether or not s is an anagram of t.
# Note 1: An anagram is a word formed by reordering the letters of another word.
# Note 2: This program is case sensitive (since it was not specified in the question)


# Time complexity: O(n + m) | Space complexity: O(m + n)
# where n is the size of the string s and m is the size of the string t 
def valid_anagram(s = "", t = ""):

    hist_s = _histogram(s)
    hist_t = _histogram(t)

    return hist_s == hist_t 


def _histogram(string):
    hist = dict()
    for char in string:
        hist[char] = hist.get(char, 0) + 1
    return hist


def main():
    # Test cases:
    assert valid_anagram(s = "cat", t = "tac")
    assert not valid_anagram(s = "Abba", t = "Bbaa")
    assert not valid_anagram(s = "abaa", t = "abba")
    assert valid_anagram(s = "listen", t = "silent")
    assert not valid_anagram(s = "program", t = "function")
    print("OK: passed all test cases!")


if __name__ == "__main__":
    main()

