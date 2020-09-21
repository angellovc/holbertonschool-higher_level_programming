#!/usr/bin/node
const logHistory = [];

exports.logMe = function (item) {
  logHistory.push(item);
  console.log(`${logHistory.length - 1}: ${item}`);
};
