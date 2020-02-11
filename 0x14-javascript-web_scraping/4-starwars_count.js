#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    let counter = 0;
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const charac of film.characters) {
        if (charac.search('/18/') > 0) {
          counter++;
        }
      }
    }
    console.log(counter);
  } else { console.log(error); }
});
