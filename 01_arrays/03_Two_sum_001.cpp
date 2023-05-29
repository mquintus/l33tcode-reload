class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        return this->hashmap_solution(nums, target);
    }

    /**
     * The loop-in-loop solution uses time complexity of O(n^2) 
     */    
    vector<int> naive_solution(vector<int>& nums, int target) {
        int complement;
        vector<int> res = {-1, -1};
        for (int i=0; i < nums.size(); i++) {
            complement = target - nums[i];
            for (int j=i+1; j < nums.size(); j++) {
                if (nums[j]==complement) {
                    res = {i, j};
                    return res;
                }
            }
        } 
        return res;
    }


    /**
     * Using a hashmap, the time complexity reduces to O(n), that is when 
     * looping the original vector, each element is iterated (O(n)) and then stored
     * into the hashmap (O(1)).
     */
    vector<int> hashmap_solution(vector<int>& nums, int target) {
        std::unordered_map<int, int> positions;
        for (int i=0; i < nums.size(); i++) {
            int complement = target - nums[i];
            auto c_position = positions.find(complement);
            if (c_position != positions.end()) {
                return {c_position->second, i};
            }
            positions[nums[i]] = i;
        } 
        return {-1, -1};
    }
    
};
