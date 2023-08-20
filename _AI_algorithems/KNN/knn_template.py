from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# dataframes
df = datasets.load_iris()
y = df['party'].values
X = df.drop('party', axis=1).values

# stratify make the labels to be distributed in train and test sets as they are in the original dataset
# y is the list or array containing the label
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, randon_ttate=21, stratify=y)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

# The accuracy
score = knn.score(X_test, y_test)