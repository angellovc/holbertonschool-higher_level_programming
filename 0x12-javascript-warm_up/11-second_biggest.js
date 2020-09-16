#!/usr/bin/node
let i;
let max = 0;
let secondMax = 0;
for (i = 2; i < process.argv.length; i++) {
  if (max < process.argv[i]) { secondMax = max; max = parseInt(process.argv[i]); }
}
console.log(secondMax);
