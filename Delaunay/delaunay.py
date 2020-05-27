
import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial import Delaunay

# Read data

points = np.genfromtxt('data.txt',delimiter=',')

plt.scatter(points[:,0],points[:,1])

plt.show()

tri = Delaunay(points)

plt.triplot(points[:,0],points[:,1],tri.simplices.copy())

plt.show()
