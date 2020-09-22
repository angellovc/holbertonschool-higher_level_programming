#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (_, response) {
  console.log(JSON.parse(response.body).title);
});
