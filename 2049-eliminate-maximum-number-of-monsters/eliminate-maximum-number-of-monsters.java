class Solution {
    public int eliminateMaximum(int[] dist, int[] speed) {

        int n = dist.length;
        float [] time = new float[n];
        for(int i=0;i<n;i++){

                time[i] = (float)dist[i]/speed[i];

        }
      
        Arrays.sort(time);
        int cnt = 0;
     
        for(int i=0;i<n;i++){
            if (time[i]>i)
                cnt+=1;
            else
                break;

        }
           
        return cnt;
        
    }
}