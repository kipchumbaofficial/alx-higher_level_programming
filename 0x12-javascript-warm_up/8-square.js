#!/usr/bin/node

// Prints a square

const { argv } = require('node:process');

if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  let i = 0;
  const size = Number(argv[2]);
  while (i < size) {
    let j = 0;
    let row = '';
    while (j < size) {
      row += 'x';
      j++;
    }
    console.log(row);
    i++;
  }
}
