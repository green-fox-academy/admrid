'use strict';
// - Create a variable named `ai` with the following content: `[3, 4, 5, 6, 7]`
// - Log the sum of the elements in `ai` to the console

let ai = [3, 4, 5, 6, 7];
let result = 0;

for (let i = 0, l = ai.length; i < l; i++){
  result += ai[i];
}

console.log(result);