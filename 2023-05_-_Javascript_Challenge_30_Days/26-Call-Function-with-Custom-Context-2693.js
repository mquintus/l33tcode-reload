/**
 * @param {Object} context
 * @param {any[]} args
 * @return {any}
 */
Function.prototype.callPolyfill = function(context, ...args) {
    /**
     * Idea: 
     * 1. loop the dict "context", extract key and value,
     * and assign them onto "this[key] = value;"
     * 2. call this()
     */
}

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */
