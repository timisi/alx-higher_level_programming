#!/usr/bin/node
// JS Script
require('request').get(process.argv[2], function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    let res = {};
    let temp = JSON.parse(body);
    for (let i = 0; i < temp.length; i++) {
      if (temp[i].completed) {
        if (!(temp[i].userId in res)) {
          res[temp[i].userId] = 0;
        }
        res[temp[i].userId] += 1;
      }
    }
    console.log(res);
  }
});
