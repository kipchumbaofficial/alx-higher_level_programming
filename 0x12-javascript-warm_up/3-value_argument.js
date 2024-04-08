#!/usr/bin/node
// Gets length of an array

function arrayLength (array) {
  let len = 0;
  for (const _ of array) { // eslint-disable-line no-unused-vars
    len++;
  }
  return len;
}

// Print out first argument

const { argv } = require('node:process');

if (arrayLength(argv) === 2) {
  console.log('No argument');
} else if (arrayLength(argv) > 2) {
  console.log(argv[2]);
}
