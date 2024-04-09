#!/usr/bin/node

// second largest

function finder (arr) {
  arr.sort(function (a, b) {
    return Number(b) - Number(a);
  });
  return arr[1];
}

const { argv } = require('node:process');

const len = argv.length;

if (len === 2 || len === 3) {
  console.log(0);
} else {
  const args = argv.slice(2);
  console.log(finder(args));
}
