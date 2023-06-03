/**
 * @param {number[]} nums
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;
};

ArrayWrapper.prototype.valueOf = function() {
    var sum = 0;
    for (el of this.nums) {
        sum += el;
    }
    return sum;
}

ArrayWrapper.prototype.toString = function() {
    var myStr = "[";
    var i = 0;
    for (el of this.nums) {
        myStr += el.toString();
        if (i++ < this.nums.length - 1) {
            myStr += ','
        }
    }
    myStr += ']';
    return myStr;
    
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
