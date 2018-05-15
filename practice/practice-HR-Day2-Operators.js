'use strict';

let mealCost = parseFloat(10.25);
let tipPercent = parseInt(17);
let taxPercent = parseInt(5);


function main() {
    let meal_cost = mealCost;
    let tip_percent = tipPercent;
    let tax_percent = taxPercent;
    
    console.log('The total meal cost is', Math.round(meal_cost + (meal_cost / 100 * tip_percent) + (meal_cost / 100 * tax_percent)), 'dollar');
}

main();



function precisionRound(number, precision) {
    var factor = Math.pow(10, precision);
    return Math.round(number * factor) / factor;
}

console.log(precisionRound(1234.5678, 1));
// expected output: 1234.6

console.log(Math.round(1234.5678));
