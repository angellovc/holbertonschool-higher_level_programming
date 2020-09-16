#!/usr/bin/node
function factorial (number) {
  let current = 0;
  if (number > 1) { current = factorial(number - 1); }
  if (current === 0) { return (1); }
  return (number * current);
}
console.log(factorial(parseInt(process.argv[2])));
