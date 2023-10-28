# Given two strings representing sentences, return the words that are 
# not common to both strings (i.e. the words that only appear in one 
# of the sentences). You may assume that each sentence is a sequence 
# of words (without punctuation) correctly separated using space characters.

# Essentially all we have to do to solve this problem  is find the 
# symmetric difference between the two sets.

# The time complexity here is kinda tricky, because inserting, deleting and lookup in
# set is O(1), but, since we're inserting strings, it will be O(s). Therefore, we have
# O(n + m + n * s1 + m * s2) time | O(n + m + n * s1 + m * s2) space
def uncommon_words(sentence1 = "", sentence2 = ""):
    lst1 = sentence1.split()                # O(n)
    lst2 = sentence2.split()                # O(m)
    set1 = set(lst1)                        # O(n * s1) - where s1 is the size of strings stored in lst1
    set2 = set(sentence2.split())           # O(m * s2) - where s2 is the size of strings stored in lst2
    return set1.symmetric_difference(set2)  # O(n*s1 + m*s2) 


def main():
    # Test cases: 
    # TC01:
    sentence1 = "the quick"
    sentence2 = "brown fox"
    expected = ["the", "quick", "brown", "fox"]
    assert all(word in expected for word in uncommon_words(sentence1, sentence2)), "Failed TC01."
    # TC02:
    sentence1 = "the tortoise beat the haire"
    sentence2 = "the tortoise lost to the haire"
    expected = ["beat", "to", "lost"]
    assert all(word in expected for word in uncommon_words(sentence1, sentence2)),"Failed TC02."
    # TC03:
    sentence1 = "copper coffee pot"
    sentence2 = "hot coffee pot"
    expected = ["copper", "hot"]
    assert all(word in expected for word in uncommon_words(sentence1, sentence2)), "Failed TC03."
    # TC04:
    sentence1 = "copper coffee"
    sentence2 = "copper coffee"
    expected = []
    assert all(word in expected for word in uncommon_words(sentence1, sentence2)), "Failed TC04."

if __name__ == "__main__":
    main()

