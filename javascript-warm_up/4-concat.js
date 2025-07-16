#!/usr/bin/node

// prints the first argument passed

const arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
