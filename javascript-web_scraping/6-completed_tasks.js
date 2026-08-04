#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  const todos = JSON.parse(body);
  const completedCounts = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (completedCounts[todo.userId]) {
        completedCounts[todo.userId]++;
      } else {
        completedCounts[todo.userId] = 1;
      }
    }
  }

  console.log(completedCounts);
});
