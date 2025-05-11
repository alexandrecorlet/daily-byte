"""
Given two strings representing sentences, return the words 
that are not common to both strings (i.e. the words that only 
appear in one of the sentences). You may assume that each sentence 
is a sequence of words (without punctuation) correctly separated 
using space characters.
"""

# Time complexity: O(n + m) | Space complexity: O(n + m)
def uncommon_words(s, t):
    
    s = s.split()
    t = t.split()
    
    # Mark words that have been seen
    seenInS = set()
    seenInT = set()
    for word in s:
        seenInS.add(word)
    for word in t:
        seenInT.add(word)

    # Find uncommon words
    uncommon = []
    # word in s and not in t
    for word in seenInS:
        if word not in seenInT:
            uncommon.append(word)

    # word in t and not in s
    for word in seenInT: 
        if word not in seenInS:
            uncommon.append(word)

    return uncommon


def main():
    s = input()
    t = input()
    print(uncommon_words(s, t))


if __name__ == "__main__":
    main()

