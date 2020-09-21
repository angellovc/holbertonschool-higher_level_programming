#!/usr/bin/node
const square = require('./5-square.js');

module.exports = class Square extends square {
  charPrint (c = 'x') {
    let row;
    let column;
    let square;
    for (row = 0; row < this.height; row++) {
      square = '';
      for (column = 0; column < this.width; column++) {
        square += c;
      }
      console.log(square);
    }
  }
};
