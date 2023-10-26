// Return the letter that was randomly added to t if it exists, otherwise, return ’  ‘.
// Note: You may assume that at most one additional character can be added to t.

#include <bits/stdc++.h>
using namespace std;

// Time complexity: O(n) | Space complexity: O(n)
// where n is the length of the string s
map<char, int> histogram(string s) {
    map<char, int> histogram;
    for (char c : s)
        histogram[c]++;
    return histogram;
}

// Time complexity: O(n) | Space complexity: O(n)
// where n is the length of the string s and t (max_size(t) = n + 1 => O(n))
char spot_difference(string s, string t) {
    if (s.length() == t.length())
        return ' ';

    // Build histograms
    map<char, int> hist_s = histogram(s);
    map<char, int> hist_t = histogram(t);
    // Find added char 
    char added_char = ' ';
    for (char c : t) {
        if (hist_s[c] < hist_t[c]) {
            added_char = c;
            break;
        }
    }

    return added_char;
}

int main() {
    // Test cases 
    assert (spot_difference("foobar", "barfoot") == 't');
    assert (spot_difference("ide", "idea") == 'a');
    assert (spot_difference("coding", "ingcod") == ' ');
    assert (spot_difference("abacaba", "aabacaba") == 'a');
    printf("YAY! Passed all tests! :P\n");
    return 0;

}
