#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row, column, square;
    for (row = 0; row < this.height; row++) {
      square = '';
      for (column = 0; column < this.width; column++) {
        square += 'X';
      }
      console.log(square);
    }
  }
};
