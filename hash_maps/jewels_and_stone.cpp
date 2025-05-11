/*
 * Given a string representing your stones and another 
 * string representing a list of jewels, 
 * return the number of stones that you have that are 
 * also jewels.
 *
 * Ex: Given the following jewels and stones...
 *
 * jewels = "abc", stones = "ac", return 2
 * jewels = "Af", stones = "AaaddfFf", return 3
 * jewels = "AYOPD", stones = "ayopd", return 0
 */

#include <bits/stdc++.h>
using namespace std;

// Time complexity: O(n + m) | Space complexity: O(n)
// where n is the length of string jewels and m is the length
// of the string stones
int countJewelsAndStones(const string &jewels, const string &stones) {
    
    unordered_set<char> seen; 
    for (char jewel : jewels) {
        seen.insert(jewel);
    }

    int cnt = 0;
    for (char stone : stones) {
        if (seen.count(stone))
            ++cnt;
    }

    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    string jewels, stones;
    cin >> jewels >> stones;

    cout << countJewelsAndStones(jewels, stones) << endl;
    return 0;
}
