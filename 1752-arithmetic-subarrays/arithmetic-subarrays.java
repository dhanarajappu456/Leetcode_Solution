class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {

        int n = nums.length;
        int m = l.length;
        List<Boolean> res = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            int a = l[i];
            int b = r[i];

            int[] arr = Arrays.copyOfRange(nums, a, b + 1);

            Arrays.sort(arr);
            int diff = arr[1] - arr[0];
            int j = 2;

            while (j < arr.length) {
                if (arr[j] - arr[j - 1] != diff) {
                    res.add(false);
                    break;
                }
                j++;
            }

            if (j == arr.length) {
                res.add(true);
            }
        }

        return res;
    }
        
    
}



