'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(number) {
  let result = 0;
  for (let i = 1; i < number; i++) {
    result += i;
  }
  return result;
}

console.log(sum(20));