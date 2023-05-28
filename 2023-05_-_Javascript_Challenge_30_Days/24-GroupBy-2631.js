/**
 * @param {Function} fn
 * @return {Array}
 *
 * @author mqs
 */
Array.prototype.groupBy = function(fn) {
    var grouped = {};
    for (var i = 0 ; i < this.length; i++) {
        var mykey = fn(this[i]);
        if ((mykey in grouped) == false) {
            grouped[fn(this[i])] = [];
        }
        grouped[fn(this[i])].push(this[i]);
    }
    return grouped;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 * 
 */

