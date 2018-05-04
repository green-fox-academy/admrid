'use strict';


let a0 = 1;
let a1 = 5;
let a2 = 10;
let b0 = 10;
let b1 = 5;
let b2 = 1;


function solve(a0, a1, a2, b0, b1, b2) {
  /*
   * Write your code here.
   */
  const listA = [a0, a1, a2];
  const listB = [b0, b1, b2];
  let winForA = 0;
  let winForB = 0;
  listA.forEach((e, i) => {
      if (e > listB[i]) {
        winForA ++;
      } else if (e < listB[i]) {
        winForB ++;
      }
  })
  const partialRes = [winForA, winForB];
  return partialRes
  // console.log(winForA, winForB);
}

const result = solve(a0, a1, a2, b0, b1, b2);

console.log(result.join(" ") + "\n");
