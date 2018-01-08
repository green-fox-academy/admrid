'use strict';

var currentHours = 14;
var currentMinutes = 34;
var currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

let realHours = 23 - currentHours;
let realMinutes = 60 - currentMinutes;
let realSeconds = 60 - currentSeconds;

let allSeconds = realSeconds + realMinutes * 60 + realHours * 3600;

console.log(allSeconds);