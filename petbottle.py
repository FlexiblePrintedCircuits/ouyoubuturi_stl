import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

stl_data = mesh.Mesh.from_file('ortprdnmxcxfr.stl')
volume, cog, inertia = stl_data.get_mass_properties()

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

print("重心座標")
print(cog)

print("慣性モーメント")
print("Lx: ", inertia[0])
print("Ly: ", inertia[1])
print("Lz: ", inertia[2])

axes.add_collection3d(mplot3d.art3d.Poly3DCollection(stl_data.vectors))

scale = stl_data.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

pyplot.show()