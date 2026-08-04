#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;

  for (const film of films) {
    if (film.characters.some((character) => character.includes('/people/18/'))) {
      count++;
    }
  }

  console.log(count);
});
