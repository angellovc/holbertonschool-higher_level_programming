#!/usr/bin/node
let array;
if (process.argv.length < 4) {
  console.log(0);
} else {
  array = process.argv.slice(2, process.argv.length);
  array.sort();
  if (array[0] > 0) { array.reverse(); }
  console.log(array[1]);
}
