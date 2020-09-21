#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrence = 0;
  list.forEach(element => {
    if (element === searchElement) { occurrence += 1; }
  });
  return occurrence;
};
