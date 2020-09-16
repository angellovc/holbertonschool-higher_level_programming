#!/usr/bin/node
let i = 0;
const array = process.argv.slice(2, process.argv.length);
if (array.length > 1) { array.sort(function (a, b) { return b - a; }); i = array[1]; }
console.log(i);
