#!/usr/bin/node
let logHistory = [];

exports.logMe = function (item) {
  logHistory.push(item);
  console.log(`${logHistory.length}: ${item}`);
}
