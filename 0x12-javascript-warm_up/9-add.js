#!/usr/bin/node

// Addition

function add (a, b) {
  return a + b;
}

const { argv } = require('node:process');

console.log(add(Number(argv[2]), Number(argv[3])));
