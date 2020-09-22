#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(response.body);
    const completedTasks = {};
    let counter = 0;
    for (let i = 0; i < tasks.length; i++) {
      if (!completedTasks[tasks[i].userId]) { counter = 0; }
      if (tasks[i].completed === true) {
        counter++;
        completedTasks[tasks[i].userId] = counter;
      }
    }
    console.log(completedTasks);
  }
});
