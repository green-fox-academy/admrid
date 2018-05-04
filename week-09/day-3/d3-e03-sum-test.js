'use strict';

let test = require('tape');
let theSumming = require('./d3-e03-sum.js');

let numlist = [3, 5, 2, 4, 6]

test('adding list of numbers', function(t) {
  let actual = theSumming.sum(numlist);
  let expected = 20;

  t.equal(actual, expected);
  t.end();
});


let numlist2 = []

test('adding empyt list', function(t) {
  let actual = theSumming.sum(numlist2);
  let expected = 0;

  t.equal(actual, expected);
  t.end();
});


let numlist3 = [2]

test('adding list with 1 number', function(t) {
  let actual = theSumming.sum(numlist3);
  let expected = 2;

  t.equal(actual, expected);
  t.end();
});


let numlist4 = [null]

test('adding list with null init', function(t) {
  let expected = Error;

  t.throws(theSumming.sum.bind(null, numlist4), expected);
  t.end();
});
