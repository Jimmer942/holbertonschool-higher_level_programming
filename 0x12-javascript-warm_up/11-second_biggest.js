#!/usr/bin/node

if (typeof process.argv[2] === 'undefined' || process.argv.length === 3) {
  console.log(0);
} else {
  let max = process.argv[2];
  let max2 = process.argv[2];
  for (let i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > max) { max = process.argv[i]; }
  }
  for (let i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > max2 && process.argv[i] < max) {
      max2 = process.argv[i];
    }
  }
  console.log(max2);
}