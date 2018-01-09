'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(number) {
  let result = 1;
  for (let i = 1; i < number + 1; i++) {
    result = i * result;
  }
  return result;
}

console.log(factorio(5));