'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times 
// the 'e' letter occurs in the word stored under the same index 
// at the fruits array! Please use the map method.



let numbersOfEs = fruits.map(function(fruit) {
  console.log(fruit);
  let numberOfEs = 0 
  for (let i = 0; i < fruit.length; i++) {
    if (fruit[i] === 'e') {
      numberOfEs++
    }
  } 
  return numberOfEs
});

console.log(numbersOfEs);



// function count() {
//   let numbers = fruits.map(realCount);
//   console.log(numbers);
// }

// function realCount(fruit) {
//   let numberOfEs = 0;
//   for (let i = 0; i < fruit.length; i++) {
//     if (fruit[i] === 'e'){
//       numberOfEs++;
//     }
//   } 
//   return numberOfEs;
// }

// count();
