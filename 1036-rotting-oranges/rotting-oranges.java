class Solution {
    int m,n;
    public int orangesRotting(int[][] grid) {
        

        m =grid.length;
        n = grid[0].length;
        int fresh=0;
        LinkedList<int[]> q  = new LinkedList<int[]>();
        int[][] vis = new int[m][n];
        int[][] dir = new int[][]{{0,1},{0,-1},{1,0},{-1,0}}; 
        for(int[] arr: vis){
            Arrays.fill(arr, 0);
        }
        int ans = 0;
        for(int i=0;i<m;i++){

            for(int j =0;j<n;j++){
                if( grid[i][j]==1)
                    fresh+=1;
                if (grid[i][j]==2)
                    q.addLast(new int[]{i,j,0});
            }
        }
       
       
        while(!q.isEmpty()){

            int[] item = q.removeFirst();
            int i=item[0],j= item[1],time = item[2]; 
   
            ans = time;
            for(int[] d : dir){
                int x = i+d[0], y= j+d[1]; 

                if (!out(x,y) && vis[x][y]==0 && grid[x][y]==1){
                   
           
                    vis[x][y]=1;
                    fresh-=1;
                    q.addLast(new int[]{x,y,time+1});
                }

            }
        }

        if( fresh == 0){
         
            return ans; 
        }
           
        return -1;
        
    }

    private  boolean  out(int i, int j){

        if(i<0 || i>=m || j<0 || j>=n)
            return true;
        return false;

    }
    
}