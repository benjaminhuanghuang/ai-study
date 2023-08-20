# 3 Steps to Time Series Forecasting: LSTM with TensorFlow Keras
https://www.justintodata.com/forecast-time-series-lstm-with-tensorflow-keras/

## Dividing the Dataset into Smaller Dataframes 
using the lagged data (from t-n to t-1) to predict the target (t+10).

It is not efficient to loop through the dataset while training the model. 
So we want to transform the dataset with each row representing the historical data and the target.
```
(t-n   ... t-3 t-2 t-1) t+10
(t-n+1 ... t-2 t-1 t)   t+11
(t-n+2 ... t-1 t   t+1) t+12

```

In this way, we only need to train the model using each row of the above matrix.


Create a create_ts_files() function to convert the original dataset to the new dataset above.
at the same time, to divide the new dataset into smaller files, which is easier to process.

The function creates a folder with files. And each file contains a pandas dataframe that looks like the new dataset in the chart above.
Each of these dataframes has columns:
y, which is the target to predict. This will be the value at t + target_step (t + 10).
x_lag{i}, the value at time t + target_step – i (t + 10 – 11, t + 10 – 21, and so on), i.e., the lagged value compared to y.

- start_index: the earliest time to be included in all the historical data for forecasting.
In this practice, we want to include history from the very beginning, so we set the default of it to be 0.

- end_index: the latest time to be included in all the historical data for forecasting.
In this practice, we want to include all the history, so we set the default of it to be None.

- history_length: this is n mentioned earlier, which is the number of timesteps to look back for each forecasting.

- step_size: the stride of the history window.
Global_active_power doesn’t change fast throughout time. So to be more efficient, we can let step_size = 10. In this way, we downsample to use every 10 minutes of data in the past to predict the future amount. We are only looking at t-1, t-11, t-21 until t-n to predict t+10.

- target_step: the number of periods in the future to predict.
As mentioned earlier, we are trying to predict the global_active_power 10 minutes ahead. So this feature = 10.

- num_rows_per_file: the number of records to put in each file.
This is necessary to divide the large new dataset into smaller files.

- data_folder: the one single folder that will contain all the files.
