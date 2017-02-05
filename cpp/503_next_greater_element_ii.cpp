class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {

        int n = nums.size();
        vector<int> result;
        for (int i =0; i < n; i++)
             result.push_back(-1);
        int i;
        for (i = 0; i < n; i++) {
            int j = (i + 1) % n;
            while (i != j) {
                if (nums[j] > nums[i]) {
                    result[i] = nums[j];
                    break;
                }
                j = (j + 1) % n;
            }
        }
        return result;
    }
};