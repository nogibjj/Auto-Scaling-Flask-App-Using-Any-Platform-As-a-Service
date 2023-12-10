import matplotlib.pyplot as plt

def summary(df):
    return df.describe()

def visualize(df):
    # define species names and corresponding colors
    species_colors = {
        'Setosa': 'red',
        'Versicolor': 'green',
        'Virginica': 'blue'
    }
    # create a scatter plot for each species
    plt.figure(figsize=(10, 8)) 

    for species, color in species_colors.items():
        subset = df[df['variety'] == species]
        plt.scatter(subset['sepal.length'], subset['sepal.width'], label=species, c=color)

    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.title('Scatter Plot: Sepal Length vs. Sepal Width')
    plt.legend(title='Species')
    plt.show()
    return "displayed successfully"