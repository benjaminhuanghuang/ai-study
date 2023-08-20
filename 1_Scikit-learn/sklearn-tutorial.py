'''
From https://www.datacamp.com/community/tutorials/machine-learning-python

'''
# Import modules
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn import datasets

# Load in the `digits` data
digits = datasets.load_digits()
# or 
#digits = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra", header=None)

print("Keys of digits", digits.keys())
print('Data of digits', digits.data)
print('Target of digits',digits.target)
print('Description of digits', digits.DESCR)

# Isolate the `digits` data
digits_data = digits.data
# 1797 samples and that there are 64 features
print("Shape of data", digits_data.shape)

# Isolate the target values with `target`
digits_target = digits.target
# Inspect the shape
print("digits_target.shape: ", digits_target.shape)

# Print the number of unique labels
number_digits = len(np.unique(digits.target))

digits_images = digits.images
# images have 1797 instances that are 8 by 8 pixels big
print("digits_images.shape: ", digits_images.shape)
# reshaped images array equals digits.data
# np.all() test whether all array elements along a given axis evaluate to True.
print(np.all(digits.images.reshape((1797,64)) == digits.data))

# Figure size (width, height) in inches
fig = plt.figure(figsize=(6, 6))

# Adjust the subplots 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# For each of the 64 images
for i in range(64):
    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    # Display an image at the i-th position
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    # label the image with the target value
    ax.text(0, 7, str(digits.target[i]))


# Join the images and target labels in a list
images_and_labels = list(zip(digits.images, digits.target))

# for every element in the list 
for index, (image, label) in enumerate(images_and_labels[:8]):
    # initialize a subplot of 2X4 at the i+1-th position
    plt.subplot(2, 4, index + 1)
    # Don't plot any axes
    plt.axis('off')
    # Display images in all subplots 
    plt.imshow(image, cmap=plt.cm.gray_r,interpolation='nearest')
    # Add a title to each subplot
    plt.title('Training: ' + str(label))

# Show the plot
# plt.show()


# Create a Randomized PCA model that takes two components
from sklearn.decomposition import RandomizedPCA as PCA
randomized_pca = PCA(n_components=2)

# Fit and transform the data to the model
reduced_data_rpca = randomized_pca.fit_transform(digits.data)

# Create a regular PCA model 
pca = PCA(n_components=2)

# Fit and transform the data to the model
reduced_data_pca = pca.fit_transform(digits.data)

# Inspect the shape
reduced_data_pca.shape

# Print out the data
print(reduced_data_rpca)
print(reduced_data_pca)

colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
for i in range(len(colors)):
    x = reduced_data_rpca[:, 0][digits.target == i]
    y = reduced_data_rpca[:, 1][digits.target == i]
    plt.scatter(x, y, c=colors[i])
plt.legend(digits.target_names, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title("PCA Scatter Plot")
plt.show()