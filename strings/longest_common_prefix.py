"""
This question is asked by Microsoft. Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
"""

# Time complexity: O(k * nlogn) | Space complexity: O(1) (excluding the output)
# where n is the length of list of string s and k is the avreage length of the strings
def longest_common_prefix(strings):
    
    strings.sort()
    first = strings[0]
    last = strings[-1]

    i = 0
    lcp = []
    while i < len(first) and  first[i] == last[i]:
        lcp.append(first[i])
        i += 1

    return "".join(lcp)


def main():
    
    strings = input().split()
    print(longest_common_prefix(strings))


if __name__ == "__main__":
    main()

