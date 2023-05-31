/**
 * @param {Object} context
 * @param {any[]} args
 * @return {any}
 */
Function.prototype.callPolyfill = function(context, ...args) {
    /**
     * Idea: 
     * 1. loop the dict "context", extract key and value,
     * and assign them onto a new object 
     *    proxyObj[key] = value;
     * 2. make "this" a function of my proxyObj
     * 3. call proxyObj."this"
     */
    var proxyObj = {}

    var contextkeys = Object.keys(context);
    for (var i = 0; i < contextkeys.length; i++) {
        var mykey = contextkeys[i];
        proxyObj[mykey] = context[mykey];
    }

    var fn = this;
    proxyObj.fn = fn;
    return proxyObj.fn(...args);
}

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */
