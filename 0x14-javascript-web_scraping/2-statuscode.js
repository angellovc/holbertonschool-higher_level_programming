#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (_, response) {
  console.log('code: ' + response.statusCode);
});
