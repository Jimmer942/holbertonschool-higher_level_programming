#!/usr/bin/node

if (typeof process.argv[2] === 'undefined' ||
    isNaN(parseInt(process.argv[2], 10)) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2], 10); i++) {
    console.log('C is fun');
  }
}
