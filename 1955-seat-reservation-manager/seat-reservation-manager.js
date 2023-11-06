/**
 * @param {number} n
 */
var SeatManager = function(n) {
    
    this.last = 0
    this.alreadyUsedAndAvailable  =[]
};

/**
 * @return {number}
 */
SeatManager.prototype.reserve = function() {

    if(this.alreadyUsedAndAvailable.length===0)
        return ++this.last;
    return this.alreadyUsedAndAvailable.shift() 
 
   
    
};

/** 
 * @param {number} seatNumber
 * @return {void}
 */
SeatManager.prototype.unreserve = function(seatNumber) {
   
    this.alreadyUsedAndAvailable.push(seatNumber);
    this.alreadyUsedAndAvailable.sort((a,b)=> a-b);

}; 

/** 
 * Your SeatManager object will be instantiated and called as such:
 * var obj = new SeatManager(n)
 * var param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */