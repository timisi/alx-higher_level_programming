#!/usr/bin/node
const process = require('process');
const args = process.argv;

function factorial (a) {
  if (a === undefined) {
    return 1;
  } else {
    parseInt(a);

    if (a < 0) {
      return -1;
    } else if (a === 0) {
      return 1;
    } else {
      return (a * factorial(a - 1));
    }
  }
}

console.log(factorial(args[2]));
