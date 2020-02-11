#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let st = '';
    for (let i = 0; i < this.width; i++) { st += c; }
    for (let i = 0; i < this.height; i++) { console.log(st); }
  }
};
