var fs = require("fs");
var commonmark = require("commonmark");
var reader = new commonmark.Parser();
var writer = new commonmark.HtmlRenderer();


var mdFilePath = process.argv[2];
var htmlFilePath = process.argv[3];

var mdFile = fs.readFileSync(mdFilePath).toString();
var mdString = mdFile.toString();

var parsed = reader.parse(mdString);
var htmlString = writer.render(parsed);
fs.writeFileSync(htmlFilePath, htmlString);

process.exit(0);
