#!/usr/bin/node
const process = require('process');
const args = process.argv;

let arr = [];
if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[2]; i++) {
    for (let j = 0; j < args[2]; j++) {
      arr.push('X');
    }
    console.log(arr.join(''));
    arr = [];
  }
}
