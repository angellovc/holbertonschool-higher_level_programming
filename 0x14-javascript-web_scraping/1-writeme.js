#!/usr/bin/node
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], { encoding: 'utf-8' }, function (error) {
  if (error) {
    return console.log(error);
  }
});
