Data exploration and analysis is typically an `iterative process`, in which the data scientist takes a sample of data and performs the following kinds of task to analyze it and test hypotheses:

- Clean data to handle errors, missing values, and other issues.

- Apply statistical techniques to better understand the data, and how the sample might be expected to represent the real-world population of data, allowing for random variation.

- Visualize data to determine relationships between variables, and in the case of a machine learning project, identify features that are potentially predictive of the label.

- Revise the hypothesis and repeat the process.


NumPy provides a lot of the functionality and tools you need to work with numbers, such as arrays of numeric values.
```
import numpy as np


data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
grades = np.array(data)
print(grades)


grades.shape

avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))
```
when you start to deal with two-dimensional tables of data, the Pandas package offers a more convenient structure to work with: the DataFrame


## loc vs iloc

```
    df_students.loc[0:5]
```
The loc method returned rows with `index label` in the list of values from 0 to 5, which includes 0, 1, 2, 3, 4, and 5 (six rows). 


```
    df_students.iloc[0:5]
```
However, the iloc method returns the rows in the `positions` included in the range 0 to 5. Since integer ranges don't include the upper-bound value, this includes positions 0, 1, 2, 3, and 4 (five rows).

iloc identifies data values in a DataFrame by position, which extends beyond rows to columns. So, for example, you can use it to find the values for the columns in positions 1 and 2 in row 0, like this:
```
    df_students.iloc[0,[1,2]]
```

In the absence of an explicit index column, the rows in our DataFrame are indexed as integer values, but the columns are identified by name:
```
    df_students.loc[0,'Grade']
```

use the loc method to find indexed rows based on a filtering expression that references named columns other than the index, like this:
```
    df_students.loc[df_students['Name']=='Aisha']
```

## query
```
    df_students.loc[df_students['Name']=='Aisha']

    df_students[df_students['Name']=='Aisha']

    df_students.query('Name=="Aisha"')

    df_students[df_students.Name == 'Aisha']

```
