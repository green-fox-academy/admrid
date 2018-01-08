'use strict';

let lineCount = 7;
let lineCountHalf = lineCount / 2;

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

if (lineCount % 2 === 0) {  
  for (let i = 1; i < lineCountHalf + 1; i++) {
    console.log(' '.repeat(lineCountHalf - i) + '*'.repeat(i) + '*'.repeat(i-1));
  }
  
  for (let i = lineCountHalf; i > 0; i--) {
    console.log(' '.repeat(lineCountHalf - i) + '*'.repeat(i) + '*'.repeat(i-1));
  }
} else {
  for (let i = 1; i < lineCountHalf + 1; i++) {
    console.log(' '.repeat(lineCountHalf - i) + '*'.repeat(i) + '*'.repeat(i-1));
  }
  
  for (let i = lineCountHalf; i > 0; i--) {
    console.log(' '.repeat(lineCountHalf - i) + '*'.repeat(i) + '*'.repeat(i-1));
  }
}