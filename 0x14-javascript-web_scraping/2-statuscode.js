#!/usr/bin/node
// Get status code of a request

const url = process.argv[2];
let request = require('request');

request(url, function (error, response, body) {
    if (error) {
        console.log(error);
    } else {
        console.log('code:', reponse && response.statusCode);
    }
});
