
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
