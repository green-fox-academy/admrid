'use strict';

function Animal(){
  this.hunger = 5;
  this.thirst = 5;
  this.eat = function() {
    this.hunger -= 1;
  };
  this.drink = function() {
    this.thirst -= 1;
  };
  this.play = function() {
    this.thirst += 1;
    this.hunger += 1;
  };
}

// let allatka = new Animal();
// console.log(allatka);


function Farm(slot){
  this.slot = slot;
  this.animals = [];
  // this.freeSlot = this.slot - this.animals;


  function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
  }
  

  this.breed = function() {
    if (this.slot > this.animals.length) {
      this.animals.push(new Animal);
    }
  };

  this.slaughter = function() {
    let minHunger = this.animals[0].hunger;
    let minHungerI = 0;
    for (let i = 0; i < this.animals.length; i++) {
      if (this.animals[i].hunger < minHungerI) {
        let minHunger = this.animals[i].hunger;
        let minHungerI = i;
      }
    }
  };

  this.print = function() {
    console.log('The farm has ' + this.animals.length + 'living animals.');
    if (this.animals.length === 20) {
      console.log('We are full.');
    } else if (this.animals.length > 0) {
      console.log('We are okay.');
    } else {
      console.log('We are bankrupt.');
    }    
  };

  this.progress = function() {    

    for (let i = 0; i <this.animals.length; i++) {
      let randomNo = getRandomInt(2);
      // console.log(randomNo);
      if (randomNo === 1) {
        this.animals[i].eat()
      }
      randomNo = getRandomInt(2);
      // console.log(randomNo);
      if (randomNo === 1) {
        this.animals[i].drink()
      }
      randomNo = getRandomInt(2);
      // console.log(randomNo);
      if (randomNo === 1) {
        this.animals[i].play()
      }
    }
    // The farm should call its breed and slaughter method at the end of each day
    this.breed();
    this.slaughter();
    // The farm should print report at the end of each day
      // Print the number of sheeps
      // Print "bankrupt" if no animals left
      // Print "okay" if the number of animals is above zero and under the slot number
      // Print "full" if the number of animals are at the maximum allowed
    this.print();
  };
}

// Create a sheep farm with 20 slots
const SheepFarm = new Farm(20);

SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();
SheepFarm.breed();

SheepFarm.progress();

console.log(SheepFarm.animals); // Should log 20 Animal objects

// const button = document.querySelector('button');

// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full

