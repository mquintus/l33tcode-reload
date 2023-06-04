/**
 * @param {Array} arr
 * @return {Matrix}
 */
var jsonToMatrix = function(arr) {
    //  First step: Determine all keys
    //
    //
    var column_keys = [];
    var determine_keys = function(row) {
        if (row === null) {
            return [[]];
        }
        if (typeof row != 'object') {
            return [[]];
        }
        var column_keys = [];
        if (Array.isArray(row)) {
            for (var i = 0; i < row.length; i++) {
                var rec_res = determine_keys(row[i]);
                for (var new_path of rec_res) {
                    column_keys.push([i.toString(), ...new_path]);
                }
            }
        }
        else {
            for (var key of Object.keys(row)) {
                var rec_res = determine_keys(row[key]);
                for (var new_path of rec_res) {
                    column_keys.push([key, ...new_path]);
                }
            }
        }
        return column_keys;
    }

    var column_keys = [];
    for (var row of arr) {
         column_keys.push(...determine_keys(row));
    }

    // Second step: For each column key 
    // create the first line of the matrix (column names)
    // but also store the column key to reference the elements
    var column_names = {};
    for (var hierarchical_list of column_keys) {
        column_names[hierarchical_list.join('.')] = hierarchical_list;
    }
    matrix = [Object.keys(column_names).sort()];
    // Third step:
    // Loop all rows again and try to access the element as references in the matrix first line.
    // If it is undefined, use "".
    for (row of arr) {
        matrix_row = [];
        for (column of matrix[0]) {
            var temp = row;
            for (key of column_names[column]) {
                try {
                    // Internal restcase 77:
                    // If across the rows, an object previously was an array, the possible index range is stored.
                    // If a later object is a dict() or a string, accessing the index is successful but shouldn't be.
                    // Therefore, if we encounter an integer index: Check first if we are accessing a string.
                    if (typeof temp == "string") {
                        temp = "";
                    }
                    else{
                        temp = temp[key];
                    }
                } catch (e) {
                    temp = "";
                }
            }
            if (Array.isArray(temp)) {
                temp = "";
            }
            if (typeof temp == 'undefined') {
                temp = "";
            }
            // Internal testcase 75: 
            // [[[[1]]],[[2]],[3]]
            // must return
            // [["0","0.0","0.0.0"],["","",1],["",2,""],[3,"",""]]
            // and not
            // [["0","0.0","0.0.0"],[[[1]],[1],1],[[2],2,""],[3,"",""]]
            // Different levels of hierarchy
            // make it possible to return a value that is actually a list.
            // and this is a valid edge case.
            if (typeof temp == 'object' && temp !== null) {
                temp = "";
            }
            // Internal restcase 77:
            // 
            //
            //

            matrix_row.push(temp);
        }
        matrix.push(matrix_row);
    }
    // Return
    return matrix;
};
