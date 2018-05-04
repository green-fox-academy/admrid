'use strict';


let ar = [1, 2, 3, 4, 10, 20];


function simpleArraySum(ar) {
  /*
   * Write your code here.
   */
  let partRes = 0;
  ar.forEach(e => {
      partRes += e;
  })   
  return partRes
}

const result = simpleArraySum(ar);

console.log(result);
