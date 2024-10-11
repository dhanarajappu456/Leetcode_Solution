class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        vector<int> arr(nums.size());
        for(int i =0 ; i<nums.size();i++)
            arr[i] = i; 
        
        sort(arr.begin(),arr.end(), [&nums](int& x, int& y) {return nums[x] == nums[y] ? x<y : nums[x]< nums[y];});
        int min_id = nums.size();
        int ans  =0 ;
        for (int& i: arr) {
            ans = ans > i - min_id? ans: i - min_id; 
            min_id = min_id < i? min_id: i;
        }
        return ans;
    }
};