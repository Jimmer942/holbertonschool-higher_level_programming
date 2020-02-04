#!/usr/bin/node

if (typeof process.argv[2] === 'undefined' ||
    isNaN(parseInt(process.argv[2], 10)) === true) {
  console.log('Missing size');
} else {
  let st = '';
  for (let i = 0; i < parseInt(process.argv[2], 10); i++) {
    st += 'X';
  }
  for (let j = 0; j < parseInt(process.argv[2], 10); j++) {
    console.log(st);
  }
}
