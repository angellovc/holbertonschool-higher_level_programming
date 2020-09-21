#!/usr/bin/node

const list = require('./100-data.js').list;
let newList = [];

console.log(list);
newList = list.map((value, index) => value * index);
console.log(newList);
