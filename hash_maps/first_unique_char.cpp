/*
 * Given a string, return the index of its first unique character. 
 * If a unique character does not exist, return -1.
 */

#include <bits/stdc++.h>
using namespace std;

// Time complexity: O(n) | Space complexity: O(n)
// where n is the size of the string
int get_index_first_unique_char(const string &s) {
    
    unordered_map<char, int> hist, char2idx;
    for (int i = 0; i < (int) s.size(); ++i) {
        hist[s[i]]++;
        char2idx[s[i]] = i;
    }
   
    for (char c : s)
        if (hist[c] == 1)
            return char2idx[c];

    return -1;
}

int main() {

    string s;
    cin >> s;
    cout << get_index_first_unique_char(s) << endl;

    return 0;
}
