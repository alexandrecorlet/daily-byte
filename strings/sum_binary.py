"""
This question is asked by Apple. Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0

Examples:
"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"

"""


# Time complexity: O(n + m) | Space Complexity: O(1)
# where n is the lenght of the string a and m is the length of the string b
def sum_binary_numbers(a, b):
    
    result = []
    carry = 0 
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0:
        
        # extract the last bit of each number
        bitA = int(a[i]) if i >= 0 else 0
        bitB = int(b[j]) if j >= 0 else 0

        carry, bitResult = divmod(bitA + bitB + carry, 2)
        result.append(bitResult)

        i -= 1
        j -= 1


    if carry:
        result.append(carry)

    return "".join(map(str, result[::-1]))


def main():
    a = input()
    b = input()
    print(sum_binary_numbers(a, b))


if __name__ == "__main__":
    main()

