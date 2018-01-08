'use strict';

let lineCount = 6;


// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

for (var i = 1; i < lineCount + 1 ; i++) {
  if (i === 1) {
    console.log('%%%%%%');
  } else if (i === lineCount) {
    console.log('%%%%%%');
  } else {
    console.log('%' + ' '.repeat(i-2) + '%' + ' '.repeat(lineCount - i - 1) + '%');
  }
}

// console.log('%'.repeat(lineCount));

// for (let i = 1; i < lineCount - 2; i++) {
//     console.log('%' + ' '.repeat(i) + '%' + ' '.repeat(lineCount - 3 - i) + '%');
// }

// console.log('%'.repeat(lineCount));