#!/usr/bin/node

// Prints arguments printed and prints

let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
