using Microsoft.Extensions.ML;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AggressionScorerModel
{
    public class AggressionScorer
    {
        private readonly PredictionEnginePool<ModelInput, ModelOutput> _predictionEnginePool;

        public AggressionScorer(PredictionEnginePool<ModelInput, ModelOutput> predictionEnginePool)
        {
            _predictionEnginePool = predictionEnginePool;
        }

        public ModelOutput Predict(string input) =>
            _predictionEnginePool.Predict(new ModelInput() { Comment = input });
    }
}
