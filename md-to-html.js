var fs = require("fs");
var Remarkable = require('remarkable');
var md = new Remarkable();


var mdFilePath = process.argv[2];
var htmlFilePath = process.argv[3];

var mdFile = fs.readFileSync(mdFilePath).toString();
var mdString = mdFile.toString();

var htmlString = md.render(mdString)
fs.writeFileSync(htmlFilePath, htmlString);

process.exit(0);
