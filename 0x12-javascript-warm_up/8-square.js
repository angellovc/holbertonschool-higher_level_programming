#!/usr/bin/node
const number = process.argv[2];
let square = String();
let inner;
let outer;
if (isNaN(number) === true) {
  console.log('Missing size');
} else {
  for (outer = 0; outer < process.argv[2]; outer++) {
    square = '';
    for (inner = 0; inner < process.argv[2]; inner++) {
      square += 'X';
    }
    console.log(square);
  }
}
