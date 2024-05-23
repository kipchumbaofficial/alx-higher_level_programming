#!/usr/bin/node
// Get number of movies with Wedge Antilies

const request = require('request');
const url = process.argv[2];
let count = 0;
const id = '18';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(id)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
