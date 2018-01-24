// Create a sum method in your class which has a list of integers as parameter
// It should return the sum of the elements in the list
// Follow these steps:
// Add a new test case
// Instantiate your class
// create a list of integers
// use the t.equal to test the result of the created sum method
// Run it
// Create different tests where you
// test your method with an empyt list
// with a list with one element in it
// with multiple elements in it
// with a null
// with a string
// Run them
// Fix your code if needed


'use strict';

let numlist = [3, 5, 8, 4, 9];

let summing = {
  sum: function(numbers) {
    let result = 0;
    numbers.forEach(element => {
      if (typeof element !== 'number') {
        throw new Error(`${element} is not a number`);
      } else {
        result += element;
      }
    });
    return result;
  }
};

module.exports = summing;