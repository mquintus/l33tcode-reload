class Solution {
public:
    int search(vector<int>& nums, int target, int offset = 0) {
        if (nums.size() == 0) {
            return -1;
        }
        int pos = int(nums.size() / 2);
        int res = nums[pos];
        if (target == res) {
            return pos + offset;
        }

        vector<int> subvector;
        
        if (target < res) {
            subvector = vector<int>(nums.begin(), nums.begin() + pos);
            offset += 0;
        }
        if (target > res) {
            subvector = vector<int>(nums.begin() + pos + 1, nums.end());
            offset += pos + 1;
        }
        return search(subvector, target, offset);

    }
};
