# Given an array of integers, return whether or not two numbers sum to a given target, k.
# Note: you may not sum a number with itself.
# (c) Alexandre Corlet

# Solution #1 -> Map
# Time Complexity: O(n) | Space Complexity O(n)
# where n is the size of the list of numbers
def two_sum(numbers, k):

    seen = set()
    for number in numbers:
        complement = k - number 
        if complement in seen:
            return True
        seen.add(number)

    return False
            

"""
# Solution #2 -> Two Pointers approach
# Time Complexity: O(nlogn) | Space Complexity: O(1)
# where n is the size of the list of numbers
def two_sum(numbers, k):

    numbers.sort()
    i, j = 0, len(numbers) - 1
    while i < j:
        s = numbers[i] + numbers[j]
        if s < k:
            i += 1
        elif s == k:
            return True 
        else:
            j -= 1

    return False 
"""


"""
# Solution #3
# Time Complexity: O(n^2) | Space Complexity: O(1)
# where n is the size of the list of numbers
def two_sum(numbers, k):

    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == k:
                return True 

    return False
"""

    
def main():
    # Test cases:
    assert two_sum([1, 3, 8, 2], 10)
    assert not two_sum([3, 9, 13, 7], 8)
    assert two_sum([4, 2, 6, 5, 2], 4)
    print("OK: passed all test cases!")


if __name__ == "__main__":
    main()

