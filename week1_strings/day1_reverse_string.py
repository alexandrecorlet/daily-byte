# Given a string, reverse all of its characters and return the resulting string.
# author: alexandre corlet

# Solution 1: Time Complexity O(n) | Space Complexity O(n)
# where n is the size of the string 
#def reverse_string(s):
#    result = ""
#    for i in range(len(s) - 1, -1, -1):
#        result += s[i];
#    return result

# Solution 2: Time Complexity O(n) | Space Complexity O(n)
# where n is the size of the string
def reverse_string(s):
    return s[::-1]


def main():
    # tests
    assert reverse_string("Cat") == "taC"
    assert reverse_string("The Daily Byte") == "etyB yliaD ehT"
    assert reverse_string("civic") == "civic"

    print("OK tests passed!")


if __name__ == "__main__":
    main()

