'use strict';

let ccyPair = 'GBPAUD';
let date = '2017-01-01';
let rate = 1.4;


let rateStorage = [];


/*
 * Complete the parseStatementNumber function below.
 */


function parseStatementNumber(numberString) {
  if (numberString.match('^\d{1,3}([,\s\_]\d{3})*(\.\d{2})?$')) {
    return numberString
  } else if (numberString.match('^\d{1,3}([\.\s\_]\d{3})*(\,\d{2})?$')){
    return numberString
  } else {
    return null
  }
}

storeRate(ccyPair, date, rate);
console.log(fetchRate('GBPAUD', '2017-01-01'));

console.log(rateStorage);
