#!/usr/bin/node

// Print multiple times

const { argv } = require('node:process');

if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < Number(argv[2])) {
    console.log('C is fun');
    i++;
  }
}
