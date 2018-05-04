'use strict';

var students = [
  {'name': 'Rezso', 'age': 9.5, 'candies': 2},
  {'name': 'Gerzson', 'age': 10, 'candies': 1},
  {'name': 'Aurel', 'age': 7, 'candies': 3},
  {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function logCandies(listOfStudents) {
  listOfStudents.forEach(student => {
    if (student.candies > 4) {
      console.log(student.name);
    }
  });
}

function logAvgCandies(listOfStudents) {
  let numOfCandies = 0;
  listOfStudents.forEach(student => {
    numOfCandies += student.candies
  });
  let avgNumOfCandies = numOfCandies / students.length;
  return avgNumOfCandies;
}


logCandies(students);
console.log(logAvgCandies(students));
