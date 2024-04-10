#!/usr/bin/node

// A squre

const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i = 0;
      while (i < this.height) {
        let row = '';
        let j = 0;
        while (j < this.width) {
          row += c;
          j++;
        }
        console.log(row);
        i++;
      }
    }
  }
}

module.exports = Square;
