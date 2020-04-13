// ----------------------------------------------------------------------------
// -                        Intel Programming Assessment                      -
// -                            Sarvesh Thakur                                -
// ----------------------------------------------------------------------------

#include <iostream>
#include <fstream>

#include "Open3D/Open3D.h"

using namespace open3d;

int main(){

    // Read triangle mesh "test_mesh.ply" // Note: Set working directory to Open3D root folder.
    open3d::geometry::TriangleMesh mesh;
    bool success = open3d::io::ReadTriangleMeshFromPLY("examples/TestData/test_mesh.ply", mesh, true);
    std::cout << "Reading dataset successful?: " << std::boolalpha << success << std::endl;
    if (!success) return -1;

    // Visualize the dataset
    auto mesh_ptr = std::make_shared<geometry::TriangleMesh>(mesh);
    mesh_ptr->ComputeAdjacencyList(); // Sharpen the view
    open3d::visualization::DrawGeometries({mesh_ptr}, "Test Mesh",1600,900);

    // Get connected components
    auto connected_components = mesh.IdenticallyColoredConnectedComponents();

    // Print connected_components in the specified format
    for (auto & connected_component : connected_components){
        for (int node : connected_component){
            std::cout << node << " ";
        } std::cout<<std::endl;
    }

    // Write to results.txt
    std::ofstream writer("examples/TestData/Results.txt"); // Writing the results in the
    for (auto color:connected_components){
        for (unsigned int i{0}; i<color.size(); i++){
            if (i == color.size() - 1) writer << color[i];
            else writer << color[i] << " ";
        }writer << "\n";
    }

    return 0;
}