// Given two integer arrays, return their intersection.
// Note: the intersection is the set of elements that are common to both arrays.

#include <iostream>
#include <unordered_set>
#include <vector>
#include <algorithm>
using namespace std;

// O(n + m) time | O(min(n, m)) space - where n is the length of nums1
// and m is the length of nums2.
unordered_set<int> intersection(vector<int> nums1, vector<int> nums2) {

    unordered_set<int> seen(nums1.begin(), nums1.end());

    // Check which numbers belongs to both arrays nums1 and nums2
    // and compute the intersection
    unordered_set<int> intersection;
    for (int num : nums2) {
        if (seen.count(num)) { 
            intersection.insert(num);
        }
    }

    return intersection;
}

int main() {

    // Test cases 
    // TC01
    vector<int> nums1 = {2, 4, 4, 2};
    vector<int> nums2 = {2, 4};
    unordered_set<int> result = {2, 4};
    assert (intersection(nums1, nums2) == result);
    cout << "TC01: OK!" << endl;
    // TC02
    nums1 = {1, 2, 3, 3};
    nums2 =  {3, 3};
    result = {3};
    assert (intersection(nums1, nums2) == result);
    cout << "TC02: OK!" << endl;
    // TC03
    nums1 = {0, 1, 2};
    result = {0, 1, 2};
    assert (intersection(nums1, nums1) == result);
    cout << "TC03: OK!" << endl;
    // TC04
    nums1 = {0, 3, 4};
    nums2 = {1, 5, 7};
    result = {};
    assert (intersection(nums1, nums2) == result); 
    cout << "TC04: OK!" << endl;

    return 0;
}
