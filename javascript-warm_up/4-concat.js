#!/usr/bin/node

//  prints two arguments passed, in the following format: “ is

const args = process.argv.slice(2);

console.log(`${args[0]} is ${args[1]}`);
