#!/usr/bin/node
$(document).ready(() => {
  $('div#toggle_header').click(() => {
    $('header').hasClass('red') ? toggleColor('red', 'green') : toggleColor('green', 'red');
  });
});
function toggleColor (current, newClass) {
  $('header').removeClass(current);
  $('header').addClass(newClass);
}
