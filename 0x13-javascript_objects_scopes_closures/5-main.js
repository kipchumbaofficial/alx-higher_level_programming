#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
console.log(s1);
console.log(Object.getPrototypeOf(s1));
s1.print();
s1.double();
s1.print();
