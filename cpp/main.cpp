#include <iostream>

using namespace std;

class Solution {
public:
    bool tryPartition(const vector<int>& nums, const int target, const int index) {
        if (target == 0) return true;
        if (target < 0) return false;
        if (index >= nums.size()) return false;

        return tryPartition(nums, target, index + 1) || tryPartition(nums, target - nums[index], index + 1);
    }

    bool canPartition(const vector<int>& nums) {
        int sum = 0;
        for (const int num : nums) {
            sum += num;
        }

        if (sum % 2 != 0) {
            return false;
        }

        const int target = sum / 2;

        return tryPartition(nums, target, 0);

    }
};

int main() {

}