import numpy as np
from matplotlib.colors import ListedColormap
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

def plot_decision_surface_knn(knn, X, Y, voronoi=False):
    """Plot a decision surface for 2 classes, optionally
    overlaying the voronoi diagram. """
    # step size in the mesh
    h = .02
    # Create color maps
    cmap_light = ListedColormap(['lightgreen', 'lightcoral'])
    cmap_bold = ListedColormap(['green','red'])
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X['X1'].min() - 1, X['X2'].max() + 1
    y_min, y_max = X['X2'].min() - 1, X['X2'].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    fig, ax = plt.subplots(figsize=(6, 6))
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light, shading='auto')

    if voronoi:
        vor = Voronoi(X)
        voronoi_plot_2d(vor, show_points=False, ax=ax)
    # Plot also the training points
    plt.scatter(X['X1'], X['X2'], c=Y, cmap=cmap_bold, s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("k-NN Classification")
    plt.show()