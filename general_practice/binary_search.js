/*
 * Binary Search algorithm in JavaScript
 * Return Index of item if item is in the sequence, or -1.
 */

function binarySearch(target, seq, lIndex, rIndex) {

    const midIndex = Math.floor(lIndex + Math.floor((rIndex - lIndex)/2));

    if (lIndex > rIndex) {

        return -1;

    }  else if ( target === seq[midIndex] ) {

        return midIndex;

    } else if ( target > seq[midIndex] ) {
        
        return binarySearch(target, seq, midIndex + 1, rIndex);

    } else {

        return binarySearch(target, seq, lIndex, midIndex - 1);

    }

}

const data = [1,2,3,4,5,60,70, 80];
const result = binarySearch(0, data, 0, data.length - 1);
