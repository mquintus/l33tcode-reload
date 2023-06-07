/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
	return async function(...args) {
        var finished = false;
        var aborted = false;
        return new Promise(async function (resolve, reject) {
            
            const myTimeout = setTimeout(() => {
                // This is the error which is handled
                // according to network requests
                if (finished == false) {
                    aborted = true;
                    reject("Time Limit Exceeded");
                }
            }, t);
            
            try {
                var retval = await fn(...args);
                if (!aborted) {
                    finished = true;
                    clearTimeout(myTimeout);
                    resolve(retval);
                }
            } catch (retval) {
                if (!aborted) {
                    finished = true;
                    clearTimeout(myTimeout);
                    reject(retval);
                }
            };
            
        });
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
