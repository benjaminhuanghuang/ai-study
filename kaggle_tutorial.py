'''
From https://www.datacamp.com/community/tutorials/kaggle-machine-learning-eda
Data https://www.kaggle.com/c/titanic/data

'''
# Import modules
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
from sklearn.metrics import accuracy_score

# change the visualization style to a base Seaborn style
sns.set() 

# Import test and train datasets
df_train = pd.read_csv('./kaggle_data/train.csv')
df_test = pd.read_csv('./kaggle_data/test.csv')

# View first lines of training data
print(df_train.head(n=4))

print(df_train.info())

sns.countplot(x='Survived', data=df_train)
plt.show()

df_test['Survived'] = 0
df_test[['PassengerId', 'Survived']].to_csv('./kaggle_data/predictions/no_survivors.csv', index=False)

sns.countplot(x='Sex', data=df_train)

sns.factorplot(x='Survived', col='Sex', kind='count', data=df_train)

plt.show()