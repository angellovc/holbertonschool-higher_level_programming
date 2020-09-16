#!/usr/bin/node
let square = '';
if (process.argv[2]) {
  for (let outer = 0; outer < process.argv[2]; outer++) {
    square = '';
    for (let inner = 0; inner < process.argv[2]; inner++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
