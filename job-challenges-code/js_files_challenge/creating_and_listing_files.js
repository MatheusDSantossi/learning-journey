const fs = require("fs");

// Asynchronous method
fs.writeFile("textFile.txt", "This is the content of the new file.", (err) => {
  if (err) throw err;

  console.log("File created successfully!");
});

// Synchronous method
try {
  fs.writeFileSync("anotherTextFile.txt", "This is content for another file");
  console.log("Another file created successfully!");
} catch (err) {
  console.error(err);
}

// Listing files and folders
// --- Asynchronous method
fs.readdir("./", (err, files) => {
  if (err) throw err;
  console.log("Files and folders in current directory: ", files);
});

// Synchronous mthod
try {
  const files = fs.readdirSync("./");
  console.log("Files and folers (synchronous): ", files);
} catch (err) {
  console.log(err);
}
