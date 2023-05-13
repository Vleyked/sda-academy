# Translate the following code to R
import matplotlib.pyplot as plt
import seaborn as sns

# Load the iris dataset
iris = sns.load_dataset("iris")

# Create a pairplot of the dataset
sns.pairplot(iris, hue="species", diag_kind="kde", markers=["o", "s", "D"])

# Add title to the plot
plt.suptitle("Iris Species Pairplot", fontsize=24, y=1.05)

# Show plot
plt.show()
