#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

class Solution_416 {
public:
    bool tryPartition(const vector<int>& nums, const int target, const int index) {
        if (target == 0) return true;
        if (target < 0) return false;
        if (index >= nums.size()) return false;

        // 遍历所有可能的组合: 对于一个数, 只有被选中和不被选中: https://claude.ai/chat/e286233f-a973-4fe5-ab1a-dc308292e4ee
        return tryPartition(nums, target, index + 1) || tryPartition(nums, target - nums[index], index + 1);
    }

    // backtracking + recursive
    bool canPartition_1(const vector<int>& nums) {
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

    static bool canPartition_2(vector<int>& nums) {
        const int sum = accumulate(nums.begin(), nums.end(), 0); // Calculate total sum

        if (sum % 2 != 0) {
            return false; // Odd sum, cannot partition
        }

        const int target = sum / 2;

        // 初始化
        // d[2] = true, 表示在 nums 里的数字, 至少有一个组合, 相加等于 2
        vector<bool> dp(target + 1, false);
        dp[0] = true;

        // 递推公式
        // dp[i - num] = true, 意味着 在 nums 里的数字, 至少有一个组合, 相加等于 i - num
        // 既然我们可以加到 i-num, 那 现在我们又 有 num, 因此 我们也可以加到 i, 所以 dp[i] = true
        // dp[i] = dp[i] || dp[i - num]

        for (const int num : nums) {
            // 每个 num 都要遍历一遍 dp, 因为 dp[i] = dp[i] || dp[i - num]
            // 对于从 0 到 target 的每一个数 i, 都要判断 nums 里的每一个 num 是否可以通过相加得到 i
            for (int i = target; i >= num; i--) {
                dp[i] = dp[i] || dp[i - num];
            }
        }

        return dp[target];
    }
};


