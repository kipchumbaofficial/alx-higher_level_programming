#!/usr/bin/node
// Get star wars movie title

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    try {
      const jsonResponse = JSON.parse(body);
      console.log(jsonResponse.title);
    } catch (e) {
      console.log(e);
    }
  }
});
