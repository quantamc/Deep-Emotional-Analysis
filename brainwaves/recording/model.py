import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


csv_path = "./emo_raw_recordings.csv"


# Step 1: Load the data
def load_neural_data(path=csv_path):
    '''Returns the pandas dataframe'''

    if os.path.exists(csv_path) == True:
        return pd.read_csv(csv_path)

    else:
        print("No file to read from")


emo_dataframe = load_neural_data()
num_rows = emo_dataframe.shape[0]

print emo_dataframe
# Step 2: Clean the data
# count the number of missing elements (NaN) in each column
counter_nan = emo_dataframe.isnull().sum()
counter_without_nam = counter_nan[counter_nan==0]
# remove the columns with missing elements
emo_dataframe = emo_dataframe[counter_without_nam.keys()]
# list of columns (last column is the class label)
columns = emo_dataframe.columns
print(columns)

# Step 3: Create feature vectors
x = emo_dataframe.ix[:,:-1].values
print x[:, 0]
# shifting the distribution of each feature to have a mean of 0 and std of 1 (same scale)
standard_scalar = StandardScaler()
x_std = standard_scalar.fit_transform(x)

# step 4: get class labels y and then encode it into number
# get class label data
y = emo_dataframe.ix[:,-1].values
# encode the class label
class_labels = np.unique(y)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# step 5: split the data into training set and test set
test_percentage = 0.4
x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size = test_percentage, random_state = 0)

# Here the high dimensionality vector space has to be  reduced to a 2D vector space
# using Distributed Stochastic Neighbor Embedding (T-SNE)

# t distributed stochastic neighbor embedding (t-SNE) visualization
tsne = TSNE(n_components=2, random_state=0)
x_test_2d = tsne.fit_transform(x_test)

# scatter plot the sample point among the 2 classes
markers=('s', 'd')
color_map = {0:'red', 1:'blue'}
plt.figure()
for idx, cl in enumerate(np.unique(y_test)):
    plt.scatter(x=x_test_2d[y_test==cl,0], y=x_test_2d[y_test==cl,1], c=color_map[idx], marker=markers[idx], label=cl)
plt.xlabel('X in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(loc='upper left')
plt.title('t-SNE visualization of test data')
plt.show()
