'use strict';

const Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function(amt) {
      this.cash += amt;
    }
}

const Cyprus = {
  cash: 0,
  name: 'Cyprus',
  tax: '5%',
  deposit: function(amt) {
    this.cash += amt;
  }
}

const Shuffler = {
    cash: 10000,
    transfer: 1,
    pick: function() {
      if (this.transfer % 2 === 0) {
        Cyprus.deposit(1000);
      } else {
        Panama.deposit(1000);
      }
      this.cash -= 1000;
      this.transfer++;
    }
}

Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000
Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000 