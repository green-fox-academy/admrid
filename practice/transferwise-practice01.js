'use strict';

let ccyPair = 'GBPAUD';
let date = '2017-01-01';
let rate = 1.4;


let rateStorage = [];

function storeRate(ccyPair, date, rate) {
  let newRate = {
    currencyPair: ccyPair,
    dateOf: date,
    currentRate: rate.toFixed(3)
  };
  rateStorage.push(newRate);
}

/*
* Complete the fetchRate function below.
*/
function fetchRate(ccyPair, date) {
  let searchRes = [];
  rateStorage.forEach(e => {
    if (e.currencyPair === ccyPair && e.dateOf === date) {
      searchRes.push(e.currentRate);
    }
  })
  return searchRes[0];
}

storeRate(ccyPair, date, rate);
console.log(fetchRate('GBPAUD', '2017-01-01'));

console.log(rateStorage);
