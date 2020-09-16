#!/usr/bin/node
let square = '';
let inner = 0;
let outer = 0;
if (process.argv[2]) {
  for (outer = 0; outer < process.argv[2]; outer++) {
    square = '';
    for (inner = 0; inner < process.argv[2]; inner++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
