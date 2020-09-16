#!/usr/bin/node
let negative = [];
let positive = [];
let array = [];
let i;
let nIndex = 0;
let pIndex = 0;
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (i = 2; i < process.argv.length; i++) {
    if (array[i] < 0) {
      negative[nIndex] = parseInt(process.argv[i]);
      nIndex++;
    } else {
      positive[pIndex] = parseInt(process.argv[i]);
      pIndex++;
    }
  }
  if (positive.length > 0) { negative.sort(); }
  positive.sort();
  negative = negative.join(' ');
  positive = positive.join(' ');
  array = negative + positive;
  array = array.split(' ');
  if (array[0] < 0 && array[array.length - 1] > 0) {
    console.log(array[array.length - 2]);
  } else {
    console.log(array[1]);
  }
}
