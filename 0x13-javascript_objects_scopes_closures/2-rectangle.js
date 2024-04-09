#!/usr/bin/node

// Rectangle with value validation

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
}

module.exports = Rectangle;
