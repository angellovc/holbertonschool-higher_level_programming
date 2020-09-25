#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$(document).ready(() => {
  $.get(url, function (data) {
    for (const film of data.results) {
      $('#list_movies').append(`<li>${film.title}</li>`);
    }
  });
});
