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

    // dynamic programming
    static bool canPartition_2(vector<int>& nums) {
        const int sum = accumulate(nums.begin(), nums.end(), 0); // Calculate total sum

        if (sum % 2 != 0) {
            return false; // Odd sum, cannot partition
        }

        const int target = sum / 2;

        vector<bool> dp(target + 1, false);
        dp[0] = true; // Base case: sum of 0 is always possible

        for (const int num : nums) {
            // 每个 num 都要进行从 target 到 num
            // dp[i - num] = true, 意味着 我们可以加到 i-num 通过 nums 数组的组合
            // 既然我们可以加到 i-num, 那 现在我们又 有 num, 因此 我们也可以加到 i, 所以 dp[i] = true
            // 注意, 不可以 直接 dp[i] = dp[i - num], 因为前面的 dp[i] = true 会被后面的覆盖掉, 对于每个 num 我们都要进行一遍判断, 只要找出一个可以的就行,
            //
            for (int i = target; i >= num; i--) {
                if (dp[i - num]) {
                    dp[i] = true;
                }
            }
        }

        return dp[target];
    }
};
