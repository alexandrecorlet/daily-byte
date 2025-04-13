"""
Problem: Given a string, reverse all of its characters and return the resulting string.

Ex:
“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
"""

# Solution #1: Time complexity O(n) | Space complexity: O(n)
# NOTE: Don't concatenate strings directly because it is O(n) operation (string are immutable in Python)
def reverse(s):
    return s[::-1] 


def main():
    s = input()
    print(reverse(s))


if __name__ == "__main__":
    main()

