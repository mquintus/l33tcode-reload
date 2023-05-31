/**
 * @param {Object} context
 * @param {any[]} args
 * @return {any}
 */
Function.prototype.callPolyfill = function(context, ...args) {
    /**
     * Naive Idea: 
     * 1. loop the dict "context", extract key and value,
     * and assign them onto a new object 
     *    proxyObj[key] = value;
     * 2. make "this" a function of my proxyObj
     * 3. call proxyObj."this"
     *
     * Simplified idea:
     * 1. use the "context" object directly as my proxyObj
     * 2. context.fn = this
     * 3. return context.fn(...args);
     */
    context.fn = this;
    return context.fn(...args);
}

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */
