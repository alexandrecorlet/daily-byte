/*
 * This question is asked by Google. Given two integer arrays, 
 * return their intersection.
 * Note: the intersection is the set of elements that 
 * are common to both arrays.
 */

#include <bits/stdc++.h>
using namespace std;

// Time complexity: O(n + m) | Space complexity: O(n)
// where n = a.size() and m = b.size()
unordered_set<int> intersection(const vector<int> &a, const vector<int> &b) {
    
    unordered_set<int> seen;
    for (int num : a)
        seen.insert(num);

    unordered_set<int> intersection;
    for (int num : b)
        if (seen.count(num))
            intersection.insert(num);

    return intersection;
}

