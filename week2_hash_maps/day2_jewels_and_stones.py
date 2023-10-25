# Given a string representing your stones and another string representing 
# a list of jewels, return the number of stones that you have that are also jewels.
# (c) Alexandre Corlet

# Solution #1
# Time complexity: O(n + m) | Space complexity O(n)
# where n is the number of jewels and m is the number of stones
def stone_and_jewels(jewels = "", stones = ""):
    
    known_jewels = set(jewels)
    cnt = 0
    for s in stones:
        if s in known_jewels:
            cnt += 1

    return cnt


"""
# Solution #2
# Time complexity: O(n + m) | Space complexity O(n + m)
# where n is the number of jewels and m is the number of stones
def stone_and_jewels(jewels = "", stones = "" ):
    known_jewels = set(jewels) 
    return sum(1 for s in stones if s in known_jewels)
"""

def main():
    # Test cases:
    assert stone_and_jewels(jewels = "abc", stones = "ac") == 2
    assert stone_and_jewels(jewels = "Af", stones = "AaaddfFf") == 3
    assert stone_and_jewels(jewels = "AYOPD", stones = "ayopd") == 0
    print("OK: passed all test cases")


if __name__ == "__main__":
    main()

