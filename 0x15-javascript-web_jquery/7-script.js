#!/usr/bin/node
$(document).ready(() => {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(url, function (data) {
    $('div#character').text(data.name);
  });
});
