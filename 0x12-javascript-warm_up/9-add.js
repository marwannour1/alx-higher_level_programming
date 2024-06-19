#!/usr/bin/node
function add (num1, num2) {
  return num1 + num2;
}

console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
