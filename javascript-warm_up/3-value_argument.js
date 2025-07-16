#!/usr/bin/node

// prints the first argument passed

const args = process.argv.slice(2);

if (args[0] === undefined) {
  console.log('No argument');
} else if (args[0] !== undefined && args[1] === undefined) {
  console.log(args[0]);
}
