/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null) {
        return false;
     }
     if (typeof obj == 'undefined') {
         return false;
     }

     var myPrototype = Object.getPrototypeOf(obj);
     if (myPrototype === null) {
         return false;
     }
     if (myPrototype == classFunction.prototype) {
         return true;
     }
     return false;

};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
