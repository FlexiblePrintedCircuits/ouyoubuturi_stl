import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

def cube_model(scaleX=1, scaleY=1, scaleZ=1):
    scaleX = scaleX / 2
    scaleY = scaleY / 2
    scaleZ = scaleZ / 2

    vertices = np.array([\
        [-1*scaleX, -1*scaleY, -1*scaleZ],
        [+1*scaleX, -1*scaleY, -1*scaleZ],
        [+1*scaleX, +1*scaleY, -1*scaleZ],
        [-1*scaleX, +1*scaleY, -1*scaleZ],
        [-1*scaleX, -1*scaleY, +1*scaleZ],
        [+1*scaleX, -1*scaleY, +1*scaleZ],
        [+1*scaleX, +1*scaleY, +1*scaleZ],
        [-1*scaleX, +1*scaleY, +1*scaleZ]])

    faces = np.array([\
        [0,3,1],
        [1,3,2],
        [0,4,7],
        [0,7,3],
        [4,5,6],
        [4,6,7],
        [5,1,2],
        [5,2,6],
        [2,3,6],
        [3,7,6],
        [0,1,5],
        [0,5,4]])

    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    cube.remove_duplicate_polygons=True
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j],:]

    return cube

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

cube_mesh = cube_model(10,20,10)
volume, cog, inertia = cube_mesh.get_mass_properties()


print("重心座標")
print(cog)

print("慣性モーメント")
print("Lx: ", inertia[0])
print("Ly: ", inertia[1])
print("Lz: ", inertia[2])

axes.add_collection3d(mplot3d.art3d.Poly3DCollection(cube_mesh.vectors))

scale = cube_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

pyplot.show()