#!/usr/bin/node
let i;
let max = 0;
let secondMax = 0;
for (i = 2; i < process.argv.length; i++) {
  if (max < process.argv[i] || (process.argv[i] < 0 && max <= 0)) {
    secondMax = max;
    max = parseInt(process.argv[i]);
  }
}
console.log(secondMax);
