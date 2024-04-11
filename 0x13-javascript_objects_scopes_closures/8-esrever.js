#!/usr/bin/node

// Reverse a list

exports.esrever = function (list) {
  let len = list.length - 1;
  const revList = [];

  while (len >= 0) {
    revList.push(list[len]);
    len--;
  }
  return revList;
};
