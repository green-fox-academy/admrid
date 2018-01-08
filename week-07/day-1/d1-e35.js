// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//

for (var i = 1; i < 9; i++) {
  if (i % 2 === 0) {
    console.log(' % % % %');
  } else {
    console.log('% % % %');
  }
}