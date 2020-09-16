#!/usr/bin/node
let array;
let i;
if (process.argv.length < 4) {
  console.log(0);
} else {
  array = process.argv.slice(2, process.argv.length);
  array.sort();
  if (array[0] > 0) { array.reverse(); }
  i = 1;
  while (array[i] === array[i - 1]) { i++; }
  console.log(array[i]);
}
