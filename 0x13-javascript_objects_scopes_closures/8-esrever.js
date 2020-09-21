#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let newIndex = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newList[newIndex] = list[i];
    newIndex++;
  }
  return newList;
};
