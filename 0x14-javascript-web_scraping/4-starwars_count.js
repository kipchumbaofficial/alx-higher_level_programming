#!/usr/bin/node
// Get number of movies with Wedge Antilies

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let jsonResponse = JSON.parse(body);
    let results = jsonResponse['results'];
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      let character = (results[i]['characters']);
      for (let j = 0; j < character.length; j++) {
        let wedge = chars[j].endsWith('18/');
        if (wedge) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
