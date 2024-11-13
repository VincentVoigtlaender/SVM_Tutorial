import matplotlib.pyplot as plt

def plot_iris(df):
    # get subsets of the DataFrame for the different species
    setosa = df.loc[df.species == 'setosa']
    versicolor = df.loc[df.species == 'versicolor']

    # create a new figure and axis
    fig, ax = plt.subplots()

    # create a scatter plot with both subsets
    ax.scatter(setosa['sepal length (cm)'], setosa['sepal width (cm)'])
    ax.scatter(versicolor['sepal length (cm)'], versicolor['sepal width (cm)'])

    # add labels to the axes
    ax.set_xlabel('sepal length (cm)')
    ax.set_ylabel('sepal width (cm)')
    # add a legend to the plot
    ax.legend(['Iris setosa', 'Iris versicolor'], loc='upper right')
    ax.set_xlim(4.165, 7.135)
    ax.set_ylim(1.88, 4.52)
    ax.set_aspect('equal')

    return (fig, ax)
