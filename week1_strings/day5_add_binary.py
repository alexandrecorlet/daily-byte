# Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
# Note: neither binary string will contain leading 0s unless the string itself is 0


# Time complexity: O(n + m) | Space complexity O(max(n, m)))
# where n is the size of the binary sting a, and m is the 
# the size of the binary string b
def binary_sum(a, b):
    n = len(a)
    m = len(b)
    if n < m:
        a, b = b, a
        n, m = m, n

    result = [] 
    j = n - 1
    carry = 0
    for i in range(m - 1, -1, -1):
        bit_a = int(a[j])
        bit_b = int(b[i])
        result.append(str(bit_a ^ bit_b ^ carry))
        carry = bit_a & bit_b
        j -= 1

    while j > -1:
        bit_a = int(a[j])
        result.append(str(bit_a ^ carry))
        carry &= bit_a
        j -= 1

    if carry:
        result.append("1")
    
    return "".join(result[::-1])


def main():
    # Test cases: 
    assert binary_sum("1", "0") == "1"
    assert binary_sum("11", "1") == "100"
    assert binary_sum("10", "101") == "111"
    assert binary_sum("0", "0") == "0"
    assert binary_sum("1000", "110") == "1110"
    assert binary_sum("111", "1") == "1000"
    print("OK: passed all tests!")


if __name__ == "__main__":
    main()

