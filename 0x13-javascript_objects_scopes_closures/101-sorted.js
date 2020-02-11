#!/usr/bin/node
const dict = require('./101-data.js').dict;
function isEmpty (obj) { return Object.keys(obj).length === 0; }
const d = {};
for (let i = 0; ; i++) {
  const l = [];
  Object.keys(dict).forEach(function (key) {
    if (dict[key] === i) { l.push(key); delete dict[key]; }
  });
  if (isEmpty(l) === false) { d[i] = l; }
  if (isEmpty(dict)) { break; }
}
console.log(d);
