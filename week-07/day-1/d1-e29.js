'use strict';

var lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

for (var i = 1; i < lineCount + 1; i++) {
  console.log(' '.repeat(lineCount - i) + '*'.repeat(i) + '*'.repeat(i-1));
}