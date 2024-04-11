#!/usr/bin/node

// map

const list = require('./100-data.js').list;
console.log(list);

const newList = list.map((element, index) => {
  return element * index;
});
console.log(newList);
