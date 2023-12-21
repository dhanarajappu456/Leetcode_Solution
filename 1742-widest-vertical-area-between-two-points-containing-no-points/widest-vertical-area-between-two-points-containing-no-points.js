/**
 * @param {number[][]} points
 * @return {number}
 */
var maxWidthOfVerticalArea = function(points) {

    const n = points.length  
    let ans = -1
    points.sort((a,b)=>{
        return a[0]- b[0]
    })
    for(let i=1 ;i<n;i++){

        ans  =  Math.max(ans, points[i][0] - points[i-1][0])

    }
    return ans
};