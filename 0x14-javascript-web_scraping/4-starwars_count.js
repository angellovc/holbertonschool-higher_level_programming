#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, { headers: { 'Content-Type': 'application/json; charset=utf-8' } }, function (_, response) {
  const films = JSON.parse(response.body).results;
  let counter = 0;
  for (let i = 0; i < films.length; i++) {
    films[i].characters.map((value) => value === wedge ? counter++ : null);
  }
  console.log(counter);
});
