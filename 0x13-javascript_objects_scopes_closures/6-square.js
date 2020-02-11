#!/usr/bin/node
const Sqrt = require('./5-square');

module.exports = class Square extends Sqrt {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    let st = '';
    for (let i = 0; i < this.width; i++) { st += c; }
    for (let i = 0; i < this.height; i++) { console.log(st); }
  }
};
