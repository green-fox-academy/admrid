'use strict';
// - Create a variable named `p1`
//   with the following content: `[1, 2, 3]`
// - Create a variable named `p2`
//   with the following content: `[4, 5]`
// - Log to the console if `p2` has more elements than `p1`

let p1 = [1, 2, 3];
let p2 = [4, 5];

if (p1.length < p2.length) {
  console.log('Yes \`p2\` has more elements than \`p1\`');
} else if (p1.length === p2.length) {
  console.log('Yo man they are \'====\'');
} else {
  console.log('Nope, \`p2\` does not have more elements than \`p1\`');
}