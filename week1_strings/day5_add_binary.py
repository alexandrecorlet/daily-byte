# Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
# Note: neither binary string will contain leading 0s unless the string itself is 0


# Time complexity: O(n + m) | Space complexity O(max(n, m)))
# where n is the size of the binary sting a, and m is the 
# the size of the binary string b
def binary_sum(a, b):

    # Ensure both binary strings have the same length 
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Compute sum
    result = ""
    carry = 0
    for bit_a, bit_b in zip(a[::-1], b[::-1]):
        bit_a = int(bit_a)
        bit_b = int(bit_b)
        carry, bit = divmod(bit_a + bit_b + carry, 2)
        result = str(bit) + result 
    if carry:
        result = "1" + result

    return result


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

