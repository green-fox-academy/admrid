'use strict';

var lineCount = 7;

// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

for (var i = 1; i < lineCount + 1; i++) {
  console.log(' '.repeat(lineCount - i) + '*'.repeat(i) + '*'.repeat(i-1));
}

for (var i = lineCount - 1; i > 0; i--) {
  console.log(' '.repeat(lineCount - i) + '*'.repeat(i) + '*'.repeat(i-1));
}