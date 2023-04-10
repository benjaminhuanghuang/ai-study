# Programming ML.NET
By Dino Esposito, Francesco Esposito 2022
https://learning.oreilly.com/library/view/programming-ml-net/9780137383511/


- Chapter 1 Artificially Intelligent Software

- Chapter 2 An Architectural Perspective of ML.NET
  
  What is intelligent software? Any software is statically designed to be aware of the context, but only intelligent software is designed to run while `being dynamically aware of the business context`.

```
public static class ModelBuilder
{
    private static MLContext Context = new MLContext();
 
   // Main method
   public static void CreateModel(string inputDataFileName, string outputModelFileName)
   {
      // Load data
 
      // Build training pipeline
 
      // Train Model
 
      // QUICK evaluation of the model 
 
      // Save the output model 
 
   }
}
```
