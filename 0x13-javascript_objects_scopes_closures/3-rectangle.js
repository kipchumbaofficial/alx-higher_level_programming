#!/usr/bin/node

// Rectangle  with a method

class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      delete this.width;
      delete this.height;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      let row = '';
      let j = 0;
      while (j < this.width) {
        row += 'X';
        j++;
      }
      console.log(row);
      i++;
    }
  }
}

module.exports = Rectangle;
