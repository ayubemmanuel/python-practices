# 📦 Import libraries
import pandas as pd
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris # type: ignore
# 🎯 Task 1: Load and Explore the Dataset
try:
    # Load Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to pandas DataFrame
    df["species"] = df["target"].map(dict(enumerate(iris.target_names)))

    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Check data types & missing values
    print("\nData Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Clean dataset (if missing values exist)
    df = df.dropna()  # Drop rows with missing values
    print("\nDataset cleaned (if any missing values were present).")

except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# 🎯 Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Group by species & get mean of numerical columns
species_means = df.groupby("species").mean(numeric_only=True)
print("\nMean values per species:")
print(species_means)

# Interesting patterns
print("\nObservations:")
print("- Setosa flowers tend to have smaller petal length & width.")
print("- Virginica flowers generally have the largest petals.")
print("- Versicolor is in between Setosa and Virginica in most measurements.")

# 🎯 Task 3: Data Visualization
sns.set_style("whitegrid")

# 1️⃣ Line Chart - Example: Petal length trend over first 50 samples
plt.figure(figsize=(8, 5))
plt.plot(df.index[:50], df["petal length (cm)"][:50], marker="o", color="teal")
plt.title("Petal Length Trend (First 50 Samples)")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.show()

# 2️⃣ Bar Chart - Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None, palette="viridis")
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3️⃣ Histogram - Distribution of sepal length
plt.figure(figsize=(8, 5))
sns.histplot(df["sepal length (cm)"], bins=15, kde=True, color="purple")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4️⃣ Scatter Plot - Sepal length vs Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="deep")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
