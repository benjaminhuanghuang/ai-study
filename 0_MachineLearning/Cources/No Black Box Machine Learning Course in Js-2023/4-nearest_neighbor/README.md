
rename the features.js to featureFunction.js


function
```
utils.getNearest=(loc,points)=>{
   let minDist=Number.MAX_SAFE_INTEGER;
   let nearestIndex=0;

   for(let i=0;i<points.length;i++){
      const point=points[i];
      const d=utils.distance(loc,point);

      if(d<minDist){
         minDist=d;
         nearestIndex=i;
      }
   }
   return nearestIndex;
}
```
