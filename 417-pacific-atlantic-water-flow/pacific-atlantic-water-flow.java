class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int row=heights.length;
        int col=heights[0].length;

        int pacific[][]=new int[row][col];
        int atlantic[][]=new int[row][col];

        int delRow[]={1,-1,0,0};
        int delCol[]={0,0,1,-1};


        for(int i=0;i<row;i++){
            dfs(i,0,heights,pacific,heights[i][0],delRow,delCol);//first col
            dfs(i,col-1,heights,atlantic,heights[i][col-1],delRow,delCol);//last col
        }

        for(int j=0;j<col;j++){
            dfs(0,j,heights,pacific,heights[0][j],delRow,delCol);//first row
            dfs(row-1,j,heights,atlantic,heights[row-1][j],delRow,delCol);//last row
        }

        List<List<Integer>>ans=new ArrayList<>();
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(pacific[i][j]==1 && atlantic[i][j]==1){
                    List<Integer>res=new ArrayList<>();
                    res.add(i);
                    res.add(j);
                    ans.add(res);
                }
            }
        }
        return ans;
    }

    public void dfs(int i,int j,int [][]heights,int[][]visit,int height,int []delRow,int delCol[]){
        int n=heights.length;
        int m=heights[0].length;
        if(i<0 || i>=n || j<0 || j>=m || visit[i][j]==1 || heights[i][j] < height) return;
        visit[i][j]=1;
        
        for(int k=0;k<4;k++){
            int nrow=i+delRow[k];
            int ncol=j+delCol[k];

            dfs(nrow,ncol,heights,visit,heights[i][j],delRow,delCol);

        }
    }
}