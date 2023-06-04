/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    // primitives
    if (object === null) {
        return "null";
    }
    if (object === true) {
        return "true";
    }
    if (object === false) {
        return "false";
    }
    if (typeof object === 'string') {
        return '"'+object+'"';
    }
    if (typeof object === 'number') {
        return ''+object+'';
    }

    if (Array.isArray(object)) {
        var ret = "[";
        for (var i=0; i<object.length; i++) {
            ret += "" + jsonStringify(object[i]);
            if (i+1<object.length) {
                ret += ","
            }
        }
        ret += "]";
        return ret;
    } else if (typeof object == 'object') {
        var ret = "{";
        var keys = Object.keys(object);
        for (var i=0; i<keys.length; i++) {
            ret += "" + jsonStringify(keys[i]);
            ret += ":" + jsonStringify(object[keys[i]]);
            if (i+1<keys.length) {
                ret += ","
            }
        }
        ret += "}";
        return ret;
    }
};
