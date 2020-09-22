#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wedge = '18';
request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(response.body).results;
    let counter = 0;
    films.forEach(film => {
      film.characters.map((value) => value.includes(wedge) ? counter++ : null);
    });
    console.log(counter);
  }
});
