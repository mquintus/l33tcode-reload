/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    /**
     * Let's check if both are 
       a) of the same type
       b) not null
       c) Array or Object

       If Array: Do recursive equality check on each list item
       If Object: 
        - check for equality of keys
        - Do recusive equality check on each key item
       If neither Array nor Object:
        - Assume primitive data type and compare directly
     */

    if (!(typeof o2 == typeof o1)) {
        //console.log("!(typeof o2 == typeof o1)");
        return false;
    }
    if (o1 === null && o2 === null) {
        return true;
    }
    if ((Array.isArray(o1) && !Array.isArray(o2)) || (!Array.isArray(o1) && Array.isArray(o2))){
        return false;
    }
    if ((Array.isArray(o1) && Array.isArray(o2))){
        if (o1.length != o2.length) {
            return false;
        }
        for (var i = 0; i < o1.length; i++) {
            if (!areDeeplyEqual(o1[key], o2[key])) {
                //console.log("!areDeeplyEqual(o1[key], o2[key])");
                return false;
            }
        }
    }
    if (typeof o2 == 'object') {
        for (var key of Object.keys(o1)) {

            if (!(key in o2)) {
                //console.log("!(key in Object.keys(o2))");
                return false;
            }

            if (!areDeeplyEqual(o1[key], o2[key])) {
                //console.log("!areDeeplyEqual(o1[key], o2[key])");
                return false;
            }
        }
    } else {
        if (o2 != o1) {
            //console.log("o2 != o1");
            return false;
        }
    }
    return true;
};
