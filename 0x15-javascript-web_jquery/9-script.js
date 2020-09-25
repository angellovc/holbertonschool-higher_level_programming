#!/usr/bin/node
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(document).ready(() => {
  $.get(url, function (data) {
    $('#hello').text(data.hello);
  });
});
