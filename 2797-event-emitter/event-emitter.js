class EventEmitter {
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    // this is  new way of declaring the instance variable in ES 6
    // you can also use , 
    // constructor(){
    //     this.eventMap = {}
    // }
    eventMap  = {}
    subscribe(eventName, callback) {
        if(!(eventName in this.eventMap))
            this.eventMap[eventName] = new Set();
        this.eventMap[eventName].add(callback);
        console.log(this.eventMap)
        return {
            unsubscribe: () => {
                this.eventMap[eventName].delete(callback);
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const res = [];
        //coalescing operator , you can also use || operator 
        (this.eventMap[eventName] ?? []).forEach((cb)=> res.push(cb(...args)));
        return res;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */