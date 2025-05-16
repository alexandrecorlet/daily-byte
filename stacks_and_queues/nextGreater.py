from collections import deque

# Time complexity: O(n + m)
# Space complexity: O(n)
# where n is the size of nums2 and m is the size of nums2
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nextGreater = dict()
        monotonicDecreasing = deque()

        # O(n)
        for num in nums2:
            # Qual o menor que ainda esta esperando por um proximo maior?
            while monotonicDecreasing and monotonicDecreasing[-1] < num:
                nextGreater[monotonicDecreasing.pop()] = num
            # Adiciona a pilha para que esse numero espere o proximo maior
            monotonicDecreasing.append(num)

        # menores sem um proximo maior
        while monotonicDecreasing:
            nextGreater[monotonicDecreasing.pop()] = -1

        # O(m)
        return [nextGreater[num] for num in nums1]

