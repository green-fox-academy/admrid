// Write a function, that takes a string as an argument and returns a dictionary 
// with all letters in the string as keys, and numbers as values that shows how many occurrences there are.
// Create a test for that.

'use strict';

function countLetters (aString) {
  let stringDict = {};
  for (let i = 0; i < aString.length; i++) {
    if (!(i in aString)) {
      stringDict[i] = 1;
    } else {
      stringDict[i] += 1;
    }
  console.log(stringDict);
  }
}

countLetters('anna');
