#!/usr/bin/node
const process = require('process');
const args = process.argv;

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}

add(args[2], args[3]);
