#!/usr/bin/node
// Script that reads and prints the content of a fileconst fs = require('fs');

fs.readFile(filePath, 'utf8', (err, data) => {
	    if (err) throw err;
	    console.log(data);
});

