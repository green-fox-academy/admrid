
// Hello World
function upperCaser(input) {
  // SOLUTION GOES HERE
  return input.toUpperCase();
}


// Higher Order Functions
function repeat(operation, num) {
  // SOLUTION GOES HERE
  for(let i = 0; i < num; i++ ) {
    operation();
  }
}


// Basic: Map
function doubleAll(numbers) {
  // SOLUTION GOES HERE
  return numbers.map(x => x * 2);
}


// Basic: Filter
const object1 = {
  a: 'somestring',
  b: 42,
  c: false
}

console.log(object1.a);


function getShortMessages(messages) {
  // SOLUTION GOES HERE
  return messages.filter(message => message.message.length < 50).map(message => message.message);
}


// Basic: Every Some
function checkUsersValid(goodUsers) {
  return function allUsersValid(submittedUsers) {
    // SOLUTION GOES HERE

    return submittedUsers.every(function(submittedUser) {
      return  goodUsers.some(function(goodUser) {
        return goodUser.id === submittedUser.id
      })
    });  
  };
}