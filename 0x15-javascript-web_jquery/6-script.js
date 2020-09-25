#!/usr/bin/node

$(document).ready(() => {
  $('div#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});
