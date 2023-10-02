
## Create web app to collect data
```
<body>
    <div id="content">
    <h1> Data Creator‹/h1>
    <div id-"sketchPadContainer"></div>
    </div>

    <script src="js/sketchPad.js"></script>
    
    <script> 
        const sketchPad = new SketchPad(sketchPadContainer);
    </script>
</body>
```

sketchPad.js
```
class SketchPad {
  constructor(container, size = 400) {
    // create canvas and append to container
    this.canvas = document.createElement("canvas");
  }
}
```

The drawing data will be downloaded as json files
```
data.drawings[label] = sketchPad.paths;
```
