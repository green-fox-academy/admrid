// Write a function, that takes two strings and returns a boolean value 
// based on if the two strings are Anagramms or not.
// Create a test for that.

'use strict';

function anagramChecking (str1, str2) {
  let str1Sorted = str1.split('').sort().join('');
  console.log(str1Sorted);
  let str2Sorted = str2.split('').sort().join('');
  console.log(str2Sorted);
  if (str1Sorted === str2Sorted) {
    return true;
  } else {
    return false;
  }
}

console.log(anagramChecking('manna', 'manna'));

module.exports = anagramChecking;
