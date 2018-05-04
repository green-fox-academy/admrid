'use strict';

let a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]];

function diagonalDifference(a) {
  /*
   * Write your code here.
   */
  let resDiagA = 0;
  let resDiagB = 0;
  let resDiff = 0;
  a.forEach((e, i) => {
    // console.log('elem(lista): ' + e + '  index: ' + i + '  indexedik eleme: ' + e[i]);
    // console.log('elem(lista): ' + e + '  -index: ' + -i + '  -indexedik eleme: ' + e[e.length-(i+1)]);
    // console.log('\n');
    console.log(e[i]);
    console.log(e[e.length-(i+1)]);
    resDiagA += e[i];
    resDiagB += e[e.length-(i+1)];
    console.log('resDiagA: ' + resDiagA);
    console.log('resDiagB: ' + resDiagB); 
  });
  return Math.abs(resDiagA - resDiagB)
}

const result = diagonalDifference(a);

console.log(result);
