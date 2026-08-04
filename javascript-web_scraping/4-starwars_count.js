#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  console.log('Number of films:', data.results ? data.results.length : 'no results key');

  const films = data.results;
  let count = 0;

  for (const film of films) {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }

  console.log(count);
});
