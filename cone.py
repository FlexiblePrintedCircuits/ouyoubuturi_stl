import open3d as o3d

mesh = o3d.geometry.TriangleMesh. create_cone()
mesh.compute_vertex_normals()
o3d.io.write_triangle_mesh("cone.stl", mesh)