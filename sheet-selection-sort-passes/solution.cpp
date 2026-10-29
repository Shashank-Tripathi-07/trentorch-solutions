
#include <bits/stdc++.h>
using namespace std;

vector<vector<long long>> selectionSortPasses(vector<long long> nums) {
    vector<vector<long long>> passes;
    int n = nums.size();

    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;

        // Find the leftmost minimum in nums[i...n-1]
        for (int j = i + 1; j < n; j++) {
            if (nums[j] < nums[minIndex]) {
                minIndex = j;
            }
        }

        // Always swap, even if minIndex == i
        swap(nums[i], nums[minIndex]);

        // Record the array after this pass
        passes.push_back(nums);
    }

    return passes;
}
