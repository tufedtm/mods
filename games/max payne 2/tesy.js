var fs = require('fs');

var obj;

var newItem = {
    "title": "",
    "description": {
        "en": "",
        "ru": ""
    },
    "authors": [],
    "urls": [],
    "version": "",
    "new": "true"
};


console.log(newItem.title);

fs.readFile('info.json', 'utf8', function (err, data) {
    if (err) throw err;
    obj = JSON.parse(data);
});