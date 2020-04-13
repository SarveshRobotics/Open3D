# ----------------------------------------------------------------------------
# -                        Open3D: www.open3d.org                            -
# ----------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2018 www.open3d.org
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# ----------------------------------------------------------------------------

import open3d as o3d
import numpy as np
import time
import pytest
import os


def test_identically_colored_connected_components():

    # Base results
    connected_components_case_1 = [[3, 9, 12, 13, 17, 18, 23, 24, 28, 29, 34, 35, 40], [43, 56, 57, 58, 68, 69, 75, 76, 77, 78, 79, 80, 81, 82, 83], [44, 45, 46, 47, 48, 49, 50, 54, 64, 65, 66, 70, 71, 72, 73, 74]]
    connected_components_case_2 = [[0, 2, 6, 7, 8, 11], [3, 9], [4, 5, 10]]


    # Get the path to test data
    pwd = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(pwd, os.pardir, os.pardir, os.pardir, "examples",
                            "TestData")
    pcd_path_1 = os.path.join(data_dir, "test_mesh.ply")
    pcd_path_2 = os.path.join(data_dir, "test_mesh_2.ply")

    # Read triangles meshes
    mesh_1 = o3d.io.read_triangle_mesh(pcd_path_1)
    mesh_2 = o3d.io.read_triangle_mesh(pcd_path_2)

    # Get connected chains
    connected_components_1 = mesh_1.identically_colored_connected_components()
    connected_components_2 = mesh_2.identically_colored_connected_components()

    # Check test cases
    for i in range(len(connected_components_1)):
        assert connected_components_case_1[i] == list(connected_components_1[i])
        assert connected_components_case_2[i] == list(connected_components_2[i])

    print("[UnitTest][test_trianglemesh.py][identically_colored_connected_components]:Test Completed")
