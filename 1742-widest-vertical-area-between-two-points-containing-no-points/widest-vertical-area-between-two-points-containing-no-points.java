class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        

        Arrays.sort(points,(a,b)->{

                return a[0]- b[0];
        });
        int  n  = points.length;
        int ans = -1 ;
        for(int i=1 ;i<n ;i++){
            ans = Math.max(ans, points[i][0]- points[i-1][0]); 
        }
        return ans;
    }
}