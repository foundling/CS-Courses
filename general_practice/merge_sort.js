const merge = function(left, right) {

    const mergedList = [];

    while (left.length && right.length) {

        let val;

        if (left[0] <= right[0]) {

            val = left.shift();
            mergedList.push(val);

        } else {

            val = right.shift();
            mergedList.push(val);

        }

    }

    return mergedList.concat(left.length ? left : right);
};

const mergeSort = function(seq) {
    if (seq.length < 2) { 
        return seq; 
    }
    const mid = Math.floor(seq.length / 2); 
    const left = mergeSort(seq.slice(0, mid));
    const right = mergeSort(seq.slice(mid));
    return merge(left, right);
};

const data = [5, 4, 3, 2, 1, 0];

var final_list = mergeSort(data);
console.log(final_list);
