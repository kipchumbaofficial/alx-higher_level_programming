#!/usr/bin/node

// gets factorial

function factorial (n) {
  if (n <= 1 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

const { argv } = require('node:process');

console.log(factorial(Number(argv[2])));
