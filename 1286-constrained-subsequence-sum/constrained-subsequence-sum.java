class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        int n = nums.length;
        int[] t = Arrays.copyOf(nums, n);
        int maxR = t[0];
        Deque<Integer> deq = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            // First get rid of out of range indices
            while (!deq.isEmpty() && deq.peekFirst() < i - k) {
                deq.pollFirst();
            }
            
            if (!deq.isEmpty()) {
                t[i] = Math.max(t[i], nums[i] + t[deq.peekFirst()]);
            }
            
            // Maintain the deque in descending order
            // So that you can get the optimum value at once from the front
            while (!deq.isEmpty() && t[i] >= t[deq.peekLast()]) {
                deq.pollLast();
            }
            
            deq.offerLast(i);
            maxR = Math.max(maxR, t[i]);
        }
        
        return maxR;
    }
}