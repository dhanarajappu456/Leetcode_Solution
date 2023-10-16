class Solution {
    public List<Integer> getRow(int rowIndex) {
        

        List<Integer> prev= new ArrayList<Integer>(Arrays.asList(1));

        if(rowIndex ==0){

            return prev;
        }
     

        for( int i= 1;i<rowIndex+1;i++){

            List curr = new ArrayList<Integer>();

            for( int j= 0;j<rowIndex+1;j++){

                if (j==0 || j== i){

                    curr.add(1);
                }
                else{

                    curr.add(0);
                }
            }
            for( int j= 1;j<i;j++){
                
                int val = prev.get(j-1)+ prev.get(j) ;

                curr.set(j, val    );
            }
            prev  = curr;
        }

        
        
        return prev;



    }
}