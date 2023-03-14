#!/usr/bin/node
const process = require('process');
const args = process.argv;
const arr = [];

if (args.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    arr.push(args[i]);
  }
  arr.sort();
  console.log(arr[arr.length - 2]);
}
