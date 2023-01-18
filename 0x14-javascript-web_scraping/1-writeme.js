#!/usr/bin/node
const fs = require('fs');

let text = process.argv[3];

fs.writeFile(process.argv[2], text, { encoding: 'utf-8' }, (err) => {
  // catch error
  if (err) {
    console.log(err);
  }
});
