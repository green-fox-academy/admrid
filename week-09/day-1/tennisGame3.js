'use strict';

var TennisGame3 = function(player1Name, player2Name) {
  this.player2 = 0;
  this.player1 = 0;

  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

TennisGame3.prototype.getScore = function() {
  let s;
  if ((this.player1 < 4 && this.player2 < 4) && (this.player1 + this.player2 < 6)) {
    let p = ['Love', 'Fifteen', 'Thirty', 'Forty'];
    s = p[this.player1];
    return (this.player1 == this.player2) ? s + '-All' : s + '-' + p[this.player2];
  } else {
    if (this.player1 == this.player2)
      return 'Deuce';
    s = this.player1 > this.player2 ? this.player1Name : this.player2Name;
    return ((this.player1 - this.player2) * (this.player1 - this.player2) == 1) ? 'Advantage ' + s : 'Win for ' + s;
  }
};

TennisGame3.prototype.wonPoint = function(playerName) {
  if (playerName == 'player1')
    this.player1 += 1;
  else
    this.player2 += 1;

};

if (typeof window === 'undefined') {
  module.exports = TennisGame3;
}