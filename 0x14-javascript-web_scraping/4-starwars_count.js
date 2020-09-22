#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (_, response) {
  const films = JSON.parse(response.body).results;
  let counter = 0;
  films.forEach(film => {
    film.characters.map((value) => value === wedge ? counter++ : null);
  });
  console.log(counter);
});
