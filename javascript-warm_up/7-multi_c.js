#!/usr/bin/node
const x = parseInt(process.argv[2], 10);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
}

let output = '';
for (let i = 0; i < x; i++) {
  output = output + 'C is fun' + (i < x - 1 ? '\n' : '');
}

if (!isNaN(x)) {
  console.log(output);
}
