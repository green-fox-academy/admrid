'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal(says) {
  this.says = says;
}

Animal.prototype.say = function() {
  console.log(this.says)
}

var Monkey = new Animal('whuhuu');
Monkey.say()