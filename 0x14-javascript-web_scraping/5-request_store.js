#!/usr/bin/node
const request = require('request');

let url = process.argv[2];
let file = process.argv[3];
const fs = require('fs');

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err); // Print the error if one occurred
  } else {
    fs.writeFileSync(process.argv[3], response.data, { encoding: 'utf-8', flag: 'w+' });
  } catch (err) {
    console.log(err);
  }
});
