#!/usr/bin/node
const request = require('request');
request(`https://swapi.co/api/films/${process.argv[2]}/`,
  function (error, response, body) {
    if (!error) { console.log(JSON.parse(body).title); } else { console.log(error); }
  });
