import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

def model():
    vertices = np.array([\
        [3, 0, 0],
        [0, 3, 0],
        [0, 0, 0],
        [0, 0, 3]])

    faces = np.array([\
        [0,1,2],
        [0,1,3],
        [0,2,3],
        [1,2,3]])

    obj = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            obj.vectors[i][j] = vertices[f[j],:]
    
    return obj

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

pyramid_mesh = model()
volume, cog, inertia = pyramid_mesh.get_mass_properties()

print("重心座標")
print(cog)

print("慣性モーメント")
print("Lx: ", inertia[0])
print("Ly: ", inertia[1])
print("Lz: ", inertia[2])

axes.add_collection3d(mplot3d.art3d.Poly3DCollection(pyramid_mesh.vectors))

scale = pyramid_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

pyplot.show()