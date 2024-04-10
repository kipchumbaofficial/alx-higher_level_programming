#!/usr/bin/node

// Anonymous

const addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};

module.exports.addMeMaybe = addMeMaybe;
