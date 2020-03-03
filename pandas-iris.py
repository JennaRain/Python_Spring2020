# Pandas

# Import modules
print("importing modules...")
import pandas as pd

# read in csv file
iris = pd.read_csv("iris_data.csv")
print("Top five lines of iris")
print(iris.head())

# How many unique species of iris are in the dataset?
print("######################")
#species = iris.Species.unique()
#print("There are", len(species), "species:", species)

print("######################")
# Rename the columns
print("Renaming the columns...")
#fields = ["Sepal-Length", "Sepal-Width", "Petal-Length", "Petal-Width", "Species", "Treatment"]
#iris.columns = fields
#print(iris.head())

print("######################")
print("Drop first two columns...")
# Lets drop first two columns
#iris = iris.drop(["Sepal-Length", "Sepal-Width"])
#iris = iris.drop(["Sepal-Length", "Sepal-Width"], axis=1)
#print(iris.head())

print("######################")
print("What is the minimum petal length?")
# What is the minimum petal length?
#print(iris.min())
#print(iris["Petal-Length"].min())

print("######################")
print("What is the maximum petal length?")
# What is the maximum petal length?
#print(iris["Petal-Length"].max())

print("######################")
print('What is the range of petal wideth?')
# What is the range of petal width?
#print(iris["Petal-Width"].max() - iris["Petal-Width"].min())

print("######################")
print("What is the average petal width?")
# What is the average petal width?
#print(iris["Petal-Width"].sum()/len(iris))
#print(iris["Petal-Width"].mean())

print("######################")
print("How many of each species are there?")
# How many of each species are there?
#print(iris.groupby("Species").count())

print("######################")
print("What is the average petal width of each species?")
#print(iris.groupby("Species").mean())
