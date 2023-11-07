/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {

    const pac = new Set() , atl = new Set()
    const m= heights.length, n = heights[0].length;


    for(let  i=0;i<heights.length;i++){

        rec(i,0,pac,heights[i][0])
        rec(i,n-1,atl,heights[i][n-1])
    }

    for(let  j=0;j<heights[0].length;j++){

        rec(0,j,pac,heights[0][j])
        rec(m-1,j,atl,heights[m-1][j])
    }

    let  ans  = Array.from(pac).filter(item=> atl.has(item))
    return ans.map(item => JSON.parse(item))
  


    function rec(i,j,vis,prevHeight){

        if (i<0 || i>=m ||  j<0 || j>=n || vis.has(JSON.stringify([i,j])) || heights[i][j]<prevHeight){
            return 
        }
       


        const currHeight = heights[i][j]
        //console.log("curr",currHeight)
        vis.add(JSON.stringify([i,j]))
        rec(i+1,j,vis,currHeight)
        rec(i-1,j,vis,currHeight)
        rec(i,j+1,vis,currHeight)
        rec(i,j-1,vis,currHeight)





    }
    
};