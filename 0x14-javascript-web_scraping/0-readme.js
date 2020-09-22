#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], { encoding: 'utf-8' }, function (error, data) {
  if (!error) {
    process.stdout.write(data);
  } else {
    console.log(error);
  }
});
