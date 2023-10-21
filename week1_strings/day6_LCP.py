# Given an array of strings, return the longest common prefix that is shared amongst all strings.
# Note: you may assume all strings only contain lowercase alphabetical characters.

# Time Complexity O(n*m) | Space Complexity: O(m)
# where n is the size of list containing all strings
# and m is the size of the longest string in the list
def LCP(strings):
    """Find the longest common prefix (LCP) that
    is shared amongst all strings
    """
    if not strings:
        return ""
    
    ans = strings[0]
    i = len(ans)
    for s in strings:
        j = 0 
        for c1, c2 in zip(ans, s):
            if c1 == c2:
                j += 1
        i = min(i, j)

    return ans[:i]


def main():
    # Test cases:
    assert LCP(["colorado", "color", "cold"]) == "col"
    assert LCP(["a", "b", "c"]) == ""
    assert LCP(["spot", "spotty", "spotted"]) == "spot"
    assert LCP(["cccc", "cc"]) == "cc"
    assert LCP(["", "a", "b"]) == ""
    print("OK passed all test cases!")


if __name__ == "__main__":
    main()

