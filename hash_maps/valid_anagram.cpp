/*
 * Given two strings s and t return whether or not s is an anagram of t.
 * Note: An anagram is a word formed by reordering the letters of another word
 */

#include <bits/stdc++.h>
using namespace std;


// Time complexity: O(n + m) | Space complexity: O(n + m)
// where n is the length of the string s and m is the 
// length of the string t.
bool is_anagram(const string &s, const string &t) {
    
    unordered_map<char, int> hist_s, hist_t;
    for (char c : s) {
        hist_s[c]++;
    }

    for (char c : t) {
        hist_t[c]++;
    }

    return hist_s == hist_t;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    string s, t;
    cin >> s >> t;

    cout << (is_anagram(s, t) ? "true" : "false") << endl;
    return 0;

}
