#!/usr/bin/node
// Writing to a file

const fs = require('fs');
const path = process.argv[2];
const data = `${process.argv[3]}\n`;

fs.writeFile(path, data, 'utf-8', (err) => {
    if (err) {
        console.log(err);
    }
});
