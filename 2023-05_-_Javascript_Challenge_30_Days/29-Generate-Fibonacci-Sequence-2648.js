/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    var i = 0;
    var j = 0;
    var k = 1;

    while (true) {
        yield j;
        i = j;
        j = k;
        k = i + j;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
