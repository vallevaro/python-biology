# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
# In this example, we will use the Iris dataset, which is a public dataset of flower measurements
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = pd.read_csv(url, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Step 3: Create a histogram to visualize the distribution of sepal length
data['sepal_length'].plot.hist()
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.show()

# Step 4: Create a box plot to visualize the spread of petal width by species
data.boxplot(by='species', column=['petal_width'])
plt.xlabel('Species')
plt.ylabel('Petal Width (cm)')
plt.title('Spread of Petal Width by Species')
plt.show()

# Step 5: Compute basic statistics
print("Mean sepal length:", data['sepal_length'].mean())
print("Standard deviation of petal width:", data['petal_width'].std())


def analyze_correlations(data):
    # Step 1: Compute pairwise correlations
    corr = data.corr()

    # Step 2: Create a heatmap to visualize the correlations
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlations between features')
    plt.show()

    # Step 3: Print the correlation coefficients
    print(corr)


# Usage example:
analyze_correlations(data)