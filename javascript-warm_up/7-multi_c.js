#!/usr/bin/node
const x = parseInt(process.argv[2], 10);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else if (x > 0) {
  let output = '';
  for (let i = 0; i < x; i++) {
    output = output + 'C is fun' + (i < x - 1 ? '\n' : '');
  }
  console.log(output);
}
