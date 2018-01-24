'use strict';

let test = require('tape');
let anagramChecking = require('./d3-e04-anagram.js');

let string1 = 'manna';
let string2 = 'manna';

test('checking 2 strings', function (t) {
  let actual = anagramChecking(string1, string2);
  let expected = false;

  t.equal(actual, expected);
  t.end();
});