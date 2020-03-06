#!/usr/bin/node
const request = require('request');
const newDict = {};
request('http://swapi.co/api/films/' + process.argv[2], function (_error, _response, body) {
  JSON.parse(body).characters.forEach(function (element, index, array) {
    request(element, function (_err, _res, bod) {
      newDict[index] = JSON.parse(bod).name;
      if (Object.keys(newDict).length === array.length) {
        let i;
        for (i = 0; i < array.length; i++) {
          console.log(newDict[i]);
        }
      }
    });
  });
});
