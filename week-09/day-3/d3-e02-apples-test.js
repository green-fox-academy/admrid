'use strict';

let test = require('tape');
let appleVar = require('./d3-e02-apples.js');

test('getApple string return', function (t) {
  let actual = appleVar.getApple();
  let expected = 'apple';

  t.equal(actual, expected);
  t.end();
});
