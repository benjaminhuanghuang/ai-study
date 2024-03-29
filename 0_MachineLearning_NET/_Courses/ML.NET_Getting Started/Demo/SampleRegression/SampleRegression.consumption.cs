// This file was auto-generated by ML.NET Model Builder.
using Microsoft.ML;
using Microsoft.ML.Data;
using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
namespace SampleRegression.ConsoleApp
{
    public partial class SampleRegression
    {
        /// <summary>
        /// model input class for SampleRegression.
        /// </summary>
        #region model input class
        public class ModelInput
        {
            [LoadColumn(0)]
            [ColumnName(@"col0")]
            public float Col0 { get; set; }

            [LoadColumn(1)]
            [ColumnName(@"col1")]
            public float Col1 { get; set; }

            [LoadColumn(2)]
            [ColumnName(@"col2")]
            public string Col2 { get; set; }

            [LoadColumn(3)]
            [ColumnName(@"col3")]
            public string Col3 { get; set; }

            [LoadColumn(4)]
            [ColumnName(@"col4")]
            public string Col4 { get; set; }

            [LoadColumn(5)]
            [ColumnName(@"col5")]
            public string Col5 { get; set; }

            [LoadColumn(6)]
            [ColumnName(@"col6")]
            public string Col6 { get; set; }

            [LoadColumn(7)]
            [ColumnName(@"col7")]
            public string Col7 { get; set; }

            [LoadColumn(8)]
            [ColumnName(@"col8")]
            public string Col8 { get; set; }

            [LoadColumn(9)]
            [ColumnName(@"col9")]
            public float Col9 { get; set; }

            [LoadColumn(10)]
            [ColumnName(@"col10")]
            public float Col10 { get; set; }

            [LoadColumn(11)]
            [ColumnName(@"col11")]
            public float Col11 { get; set; }

            [LoadColumn(12)]
            [ColumnName(@"col12")]
            public float Col12 { get; set; }

            [LoadColumn(13)]
            [ColumnName(@"col13")]
            public float Col13 { get; set; }

            [LoadColumn(14)]
            [ColumnName(@"col14")]
            public string Col14 { get; set; }

            [LoadColumn(15)]
            [ColumnName(@"col15")]
            public string Col15 { get; set; }

            [LoadColumn(16)]
            [ColumnName(@"col16")]
            public float Col16 { get; set; }

            [LoadColumn(17)]
            [ColumnName(@"col17")]
            public string Col17 { get; set; }

            [LoadColumn(18)]
            [ColumnName(@"col18")]
            public float Col18 { get; set; }

            [LoadColumn(19)]
            [ColumnName(@"col19")]
            public float Col19 { get; set; }

            [LoadColumn(20)]
            [ColumnName(@"col20")]
            public float Col20 { get; set; }

            [LoadColumn(21)]
            [ColumnName(@"col21")]
            public float Col21 { get; set; }

            [LoadColumn(22)]
            [ColumnName(@"col22")]
            public float Col22 { get; set; }

            [LoadColumn(23)]
            [ColumnName(@"col23")]
            public float Col23 { get; set; }

            [LoadColumn(24)]
            [ColumnName(@"col24")]
            public float Col24 { get; set; }

            [LoadColumn(25)]
            [ColumnName(@"col25")]
            public float Col25 { get; set; }

        }

        #endregion

        /// <summary>
        /// model output class for SampleRegression.
        /// </summary>
        #region model output class
        public class ModelOutput
        {
            [ColumnName(@"col0")]
            public float Col0 { get; set; }

            [ColumnName(@"col1")]
            public float Col1 { get; set; }

            [ColumnName(@"col2")]
            public float[] Col2 { get; set; }

            [ColumnName(@"col3")]
            public float[] Col3 { get; set; }

            [ColumnName(@"col4")]
            public float[] Col4 { get; set; }

            [ColumnName(@"col5")]
            public float[] Col5 { get; set; }

            [ColumnName(@"col6")]
            public float[] Col6 { get; set; }

            [ColumnName(@"col7")]
            public float[] Col7 { get; set; }

            [ColumnName(@"col8")]
            public float[] Col8 { get; set; }

            [ColumnName(@"col9")]
            public float Col9 { get; set; }

            [ColumnName(@"col10")]
            public float Col10 { get; set; }

            [ColumnName(@"col11")]
            public float Col11 { get; set; }

            [ColumnName(@"col12")]
            public float Col12 { get; set; }

            [ColumnName(@"col13")]
            public float Col13 { get; set; }

            [ColumnName(@"col14")]
            public float[] Col14 { get; set; }

            [ColumnName(@"col15")]
            public float[] Col15 { get; set; }

            [ColumnName(@"col16")]
            public float Col16 { get; set; }

            [ColumnName(@"col17")]
            public float[] Col17 { get; set; }

            [ColumnName(@"col18")]
            public float Col18 { get; set; }

            [ColumnName(@"col19")]
            public float Col19 { get; set; }

            [ColumnName(@"col20")]
            public float Col20 { get; set; }

            [ColumnName(@"col21")]
            public float Col21 { get; set; }

            [ColumnName(@"col22")]
            public float Col22 { get; set; }

            [ColumnName(@"col23")]
            public float Col23 { get; set; }

            [ColumnName(@"col24")]
            public float Col24 { get; set; }

            [ColumnName(@"col25")]
            public float Col25 { get; set; }

            [ColumnName(@"Features")]
            public float[] Features { get; set; }

            [ColumnName(@"Score")]
            public float Score { get; set; }

        }

        #endregion

        private static string MLNetModelPath = Path.GetFullPath("SampleRegression.mlnet");

        public static readonly Lazy<PredictionEngine<ModelInput, ModelOutput>> PredictEngine = new Lazy<PredictionEngine<ModelInput, ModelOutput>>(() => CreatePredictEngine(), true);


        private static PredictionEngine<ModelInput, ModelOutput> CreatePredictEngine()
        {
            var mlContext = new MLContext();
            ITransformer mlModel = mlContext.Model.Load(MLNetModelPath, out var _);
            return mlContext.Model.CreatePredictionEngine<ModelInput, ModelOutput>(mlModel);
        }

        /// <summary>
        /// Use this method to predict on <see cref="ModelInput"/>.
        /// </summary>
        /// <param name="input">model input.</param>
        /// <returns><seealso cref=" ModelOutput"/></returns>
        public static ModelOutput Predict(ModelInput input)
        {
            var predEngine = PredictEngine.Value;
            return predEngine.Predict(input);
        }

    }
}
