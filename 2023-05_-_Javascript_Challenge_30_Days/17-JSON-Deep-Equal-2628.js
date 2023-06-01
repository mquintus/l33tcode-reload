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
}
