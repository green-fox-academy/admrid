'use strict';
// - Create a variable named `nimals`
//   with the following content: `["kuty", "macsk", "cic"]`
// - Add all elements an `"a"` at the end
// - try to use built in functions instead of loops

let nimals = ["kuty", "macsk", "cic"];
let animals = [];

nimals.forEach(element => {
  animals.push(element + 'a');
});

// nimals.forEach(function(e) {
//   console.log(e);
// });

console.log(animals);