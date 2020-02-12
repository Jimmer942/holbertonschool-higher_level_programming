#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed === true) {
        if (!(task.userId in completed)) { completed[task.userId] = 1; } else { completed[task.userId]++; }
      }
    }
    console.log(completed);
  } else { console.log(error); }
});
