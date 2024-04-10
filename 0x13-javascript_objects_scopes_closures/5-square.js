#!/usr/bin/node

// A square

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  size;

  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
