'use strict';
// - Create variable named `al` and assign the value `Greenfox` to it
// - Create a function called `greet` that greets it's input parameter
//     - Greeting is printing e.g. `Greetings, dear Greenfox`
//     - Prepare for the special case when no parameters are given
// - Greet `al`


let al = 'Greenfox';

function greet (somebody) {
  if (somebody === undefined) {
    console.log('Who do you think you are?');  
  } else {
    console.log('Greetings, dear ' + somebody + '!');
  }
}

greet();