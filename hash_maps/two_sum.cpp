#include <bits/stdc++.h>
using namespace std;

// Time complexity: O(n) | Space complexity: O(n)
// where n is the length of numbers
bool two_sum(const vector<int> &numbers, int target) {
    
    unordered_set<int> seen;
    for (int number : numbers) {
        int need = target - number;
        if (seen.count(need)) {
            return true;
        }
        seen.insert(number);
    }

    return false;
}

