#!/usr/bin/node
// Get number of movies with Wedge Antilies

const request = require('request');
const url = process.argv[2];
let count = 0;
const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    try {
      const jsonResponse = JSON.parse(body);
      jsonResponse.results.forEach(movie => {
        if (movie.characters.includes(wedge)) {
          count += 1;
        }
      });
      console.log(count);
    } catch (e) {
      console.log(e);
    }
  }
});
