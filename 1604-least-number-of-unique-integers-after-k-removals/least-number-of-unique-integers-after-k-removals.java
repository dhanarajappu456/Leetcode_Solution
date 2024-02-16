class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        
        
        
        Map<Integer,Integer> mp = new HashMap<>();
        
        PriorityQueue<int[]>  heap  = new PriorityQueue<>((a,b)-> a[0]-b[0]);
        
        
        for(int  num : arr){
            
            mp.put(num , mp.getOrDefault(num,0)+1);
        }
        
        
        for(Map.Entry<Integer, Integer> entry : mp.entrySet()){
            
            heap.offer(new int[]{entry.getValue(), entry.getKey()});
        }
        
        
        while(heap.size()>0 && heap.peek()[0]<=k){
            int[] pair  =heap.poll();
            k-= pair[0];
        }
        
        return heap.size();
    }
}