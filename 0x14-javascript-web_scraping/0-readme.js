#!/usr/bin/node
// Reads and print

const path = process.argv[2];
const fs = require('fs');

fs.readFile(path, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
