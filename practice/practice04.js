'use strict';

let arr = [1, 5, 3, 4, 1];
let k = 5;


function findNumber(arr, k) {
  let answer = '';
  arr.forEach(e => {
    console.log(k, e);
    if (k === e) {
      answer = 'YES';
      return answer
    } else {
      answer = 'NO';
    }
  })
}

const result = findNumber(arr, k);

console.log(result);
