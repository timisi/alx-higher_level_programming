#!/usr/bin/node

exports.addMeMaybe = function (number, newFunc) {
  number = number + 1;
  newFunc(number);
};
