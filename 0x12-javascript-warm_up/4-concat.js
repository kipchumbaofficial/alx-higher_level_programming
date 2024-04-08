#!/usr/bin/node

// Creates a sentence from arguments

function arrayLength (array) {
  let len = 0;
  for (const elements of array) { // eslint-disable-line no-unused-vars
    len++;
  }
  return len;
}

const { argv } = require('node:process');
let firstArg;
let secArg;
if (arrayLength(argv) > 2) {
  firstArg = argv[2];
  secArg = argv[3];
}
console.log(firstArg + ' is ' + secArg);
