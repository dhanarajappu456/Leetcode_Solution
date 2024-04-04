/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 /*


 function MyClass() {}

MyClass.prototype.p = 100;
const a = new MyClass();
//we cant use Object.getPrototype on the class function or any function it is meant for objet
// so we use the property calleed "prototype" on function / class function  
// this property is hidden on objects , so we can only use  Object.getPrototype on the objects to get 
// also remember prototype id in fact an object  
----------------------------------------------------
prototype hierarchy
..............................
//we can climb up the prototype ladder  whose top is a "Object protype " which is prototype of all objects
//after that is null if we climb further
------------------------------------------
more into prototype
.....................
class Animal {}; 


class Dog extends Animal  {};

Animal.prototype.p=4 
Dog.prototype.f =100

console.log(Animal.prototype) //{ p: 43 }
console.log(Dog.prototype) // Animal { f: 100 }  , its prototype is Animal protype with {f:100} included 
console.log(Object.getPrototypeOf(Dog.prototype)) //{ p: 4 },which is animal prototype 






Output:

{ p: 100 }
{ p: 100 }
true
*/
var checkIfInstanceOf = function(obj, classFunction) {
    if(obj === null|| obj === undefined || typeof classFunction !=='function'){
        console.log("hey",obj,classFunction==null);
               return false;
    }
 
    let currentPrototype  = Object.getPrototypeOf(obj)
    while(currentPrototype!=null){
       
        if (currentPrototype == classFunction.prototype){
            console.log(currentPrototype, classFunction.prototype);
            return true ;
        }
         currentPrototype  =  Object.getPrototypeOf(currentPrototype);

    }
    console.log("undefined");
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */