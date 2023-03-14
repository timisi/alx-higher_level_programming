#!/usr/bin/node

exports.callMeMoby = function (x, newFunc) {
  for (let i = 0; i < x; i++) {
    newFunc();
  }
};
