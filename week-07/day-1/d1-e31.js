'use strict';

let lineCount = 6;

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %   %
// %   %
// %   %
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

for (let i = 1; i <= lineCount ; i++) {
  if (i === 1) {
    console.log('%%%%%');
  } else if (i === lineCount) {
    console.log('%%%%%');
  } else {
    console.log('%   %');
  }
}
