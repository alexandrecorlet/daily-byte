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

    # assume the entire 0-th string is the longest common prefix
    lcp = strings[0]          
    best_lcp = len(lcp)
    # Compute the lcp
    for s in strings:
        curr_lcp = 0
        i = 0
        while i < min(best_lcp, len(s)):
            if s[i] == lcp[i]:
                curr_lcp += 1
            else:
                break
            i += 1
        best_lcp = min(best_lcp, curr_lcp)
    
    return lcp[:best_lcp] if best_lcp else ""
        
        

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

