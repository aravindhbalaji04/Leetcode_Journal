class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        map<int,int>dict;
        for(int i=0; i<n; i++){
            int remain = target - nums[i];
            if(dict.find(remain) != dict.end()){
                return {dict[remain], i};
            }else{
                dict[nums[i]] = i;
            }
        }
        return {};
    }
};
