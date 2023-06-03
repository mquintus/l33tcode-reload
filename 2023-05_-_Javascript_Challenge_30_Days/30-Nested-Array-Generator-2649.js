const flatten = function(arr) {
    const flatArray = []
    if (Array.isArray(arr)) {
        for (el of arr) {
            if (Array.isArray(el)) {
                flatArray.push(...flatten(el));
            } else {
                flatArray.push(el);
            }
        }
    } 
    return flatArray;
};

/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    for (el of flatten(arr)) {
        yield el;
    }
    
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */
