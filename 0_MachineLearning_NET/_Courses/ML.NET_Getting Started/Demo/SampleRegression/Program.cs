
// This file was auto-generated by ML.NET Model Builder. 

using System;

namespace SampleRegression.ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create single instance of sample data from first line of dataset for model input
            SampleRegression.ModelInput sampleData = new SampleRegression.ModelInput()
            {
                Col0 = 3F,
                Col2 = @"alfa-romero",
                Col3 = @"gas",
                Col4 = @"std",
                Col5 = @"two",
                Col6 = @"convertible",
                Col7 = @"rwd",
                Col8 = @"front",
                Col9 = 88.6F,
                Col10 = 168.8F,
                Col11 = 64.1F,
                Col12 = 48.8F,
                Col13 = 2548F,
                Col14 = @"dohc",
                Col15 = @"four",
                Col16 = 130F,
                Col17 = @"mpfi",
                Col18 = 3.47F,
                Col19 = 2.68F,
                Col20 = 9F,
                Col21 = 111F,
                Col22 = 5000F,
                Col23 = 21F,
                Col24 = 27F,
            };

            Console.WriteLine("Using model to make single prediction -- Comparing actual Col25 with predicted Col25 from sample data...\n\n");


            Console.WriteLine($"Col0: {3F}");
            Console.WriteLine($"Col2: {@"alfa-romero"}");
            Console.WriteLine($"Col3: {@"gas"}");
            Console.WriteLine($"Col4: {@"std"}");
            Console.WriteLine($"Col5: {@"two"}");
            Console.WriteLine($"Col6: {@"convertible"}");
            Console.WriteLine($"Col7: {@"rwd"}");
            Console.WriteLine($"Col8: {@"front"}");
            Console.WriteLine($"Col9: {88.6F}");
            Console.WriteLine($"Col10: {168.8F}");
            Console.WriteLine($"Col11: {64.1F}");
            Console.WriteLine($"Col12: {48.8F}");
            Console.WriteLine($"Col13: {2548F}");
            Console.WriteLine($"Col14: {@"dohc"}");
            Console.WriteLine($"Col15: {@"four"}");
            Console.WriteLine($"Col16: {130F}");
            Console.WriteLine($"Col17: {@"mpfi"}");
            Console.WriteLine($"Col18: {3.47F}");
            Console.WriteLine($"Col19: {2.68F}");
            Console.WriteLine($"Col20: {9F}");
            Console.WriteLine($"Col21: {111F}");
            Console.WriteLine($"Col22: {5000F}");
            Console.WriteLine($"Col23: {21F}");
            Console.WriteLine($"Col24: {27F}");
            Console.WriteLine($"Col25: {13495F}");



            // Use the model and Prediction Engine to predict on new sample data
            var predictionResult = predEngine.Predict(sampleData);

            Console.WriteLine($"\n\nPredicted Col25: {predictionResult.Score}\n\n");
            Console.WriteLine("=============== End of process, hit any key to finish ===============");
            Console.ReadKey();
        }
    }
}
