### Data Manipulation Steps
1. Loading the Dataset:  
To begin the analysis, I loaded the Iris dataset from a remote source using the Pandas library. The dataset contains information about Sepal Length, Sepal Width, Petal Length, Petal Width, and the species variety of iris flowers. This dataset is commonly used for various data analysis and machine learning tasks.

2. Data Exploration:  
I explored the dataset's dimensions, which provides an understanding of the dataset's size. The dataset consists of 150 rows and 5 columns, indicating that we have 150 data points and 5 attributes for each data point.

3. Summary Statistics:  
Next, I computed summary statistics for the numerical attributes in the dataset. This includes count, mean, standard deviation, minimum, maximum, and quartiles. These statistics offer insights into the distribution and central tendencies of the data.

4. Data Visualization:  
I created a scatter plot to visualize the relationship between Sepal Length and Sepal Width for different species (Setosa, Versicolor, and Virginica) within the dataset. Each species is represented by a distinct color on the plot, making it easier to distinguish between them.

5. Data Analysis by Filtering:  
Data manipulation is often necessary to extract specific information. I demonstrated the following important operations 

- Filtering Data - I filtered the dataset to include only rows where Sepal Length is greater than 5.5. This operation reduces the dataset to a subset of data points that meet the specified condition.

- Sorting Data - I sorted the dataset based on the Petal Length attribute in ascending order. This operation allows us to arrange the data in a specific order, which can be useful for various analyses.

- Calculating Mean - I calculated the mean Sepal Length and Sepal Width for each species in the dataset using a group-by operation. This provides insights into the average characteristics of different iris species.
