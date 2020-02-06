#!/usr/bin/node

if (typeof process.argv[2] === 'undefined' || process.argv.length === 3) {
  console.log(0);
} else {
  let max = process.argv[2];
  let max2 = 0;
  for (let i = 3; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max) { max = parseInt(process.argv[i]); }
  }
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max2 && parseInt(process.argv[i]) < max) {
      max2 = parseInt(process.argv[i]);
    }
  }
  console.log(max2);
}
