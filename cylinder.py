import open3d as o3d

mesh = o3d.geometry.TriangleMesh.create_cylinder()
mesh.compute_vertex_normals()
o3d.io.write_triangle_mesh("cylinder.stl", mesh)