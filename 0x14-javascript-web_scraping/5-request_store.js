#!/usr/bin/node
// Read HTML and write to a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(path, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
