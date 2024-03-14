# from numpy import pi, cos, sin, sqrt, arange
# import matplotlib.pyplot as pp

# num_pts = 100
# indices = arange(0, num_pts, dtype=float) + 0.5

# r = sqrt(indices/num_pts)
# theta = pi * (1 + 5**0.5) * indices

# pp.scatter(r*cos(theta), r*sin(theta))
# pp.show()

# 3D
from numpy import pi, cos, sin, arccos, arange
import mpl_toolkits.mplot3d
import matplotlib.pyplot as pp

num_pts = 100
indices = arange(0, num_pts, dtype=float) + 0.5

phi = arccos(1 - 2*indices/num_pts)
theta = pi * (1 + 5**0.5) * indices

x, y, z = cos(theta) * sin(phi), sin(theta) * sin(phi), cos(phi)

pp.figure().add_subplot(111, projection='3d').scatter(x, y, z)
pp.show()