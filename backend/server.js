const express = require("express");
const path = require("path");
const app = express();
const PORT = process.env.PORT || 8000;

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.post("/api/analyze", (req, res) => {
  console.log("analyzing some text..");
  const spawn = require("child_process").spawn;
  console.log(req.body.text);
  let dataToSend = {};
  const python = spawn("python", [
    __dirname + "/PythonScript/analyzeText.py",
    req.body.text,
  ]);
  python.stdout.on("data", function (data) {
    console.log("Pipe data from python script ...");
    dataToSend = data.toString();
  });
  python.stderr.on("data", (data) => {
    // As said before, convert the Uint8Array to a readable string.
    console.log(data.toString());
  });
  python.on("close", (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    data = dataToSend.replace(/'/g, '"');
    res.status(200).send(JSON.parse(data));
  });
});

//serve Frontend
if (process.env.NODE_ENV === "production") {
  app.use(express.static(path.join(__dirname, "../frontend/build")));
  app.get("*", (req, res) =>
    res.sendFile(__dirname, "../", "frontend", "build", "index.html")
  );
} else {
  app.get("/", (req, res) => {
    res.status(200).json({ message: "Welcome to the API" });
  });
}

app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));
