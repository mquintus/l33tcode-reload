/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (classFunction === null || typeof classFunction !== "function") {
        return false;
     }
    if (obj === null) {
        return false;
     }
     if (typeof obj == 'undefined') {
         return false;
     }

     var myPrototype = Object.getPrototypeOf(obj);
     while (myPrototype !== null) {
        if (myPrototype == classFunction.prototype) {
            return true;
        }
        myPrototype = Object.getPrototypeOf(myPrototype);
     }
     return false;

};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
