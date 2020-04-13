import open3d as o3d

if __name__ == "__main__":

    # Read the dataset
    triangle_mesh = o3d.io.read_triangle_mesh("examples/TestData/test_mesh.ply")

    # Get the connected components
    connected_components = triangle_mesh.identically_colored_connected_components()

    # Print connected_components in the specified format
    for i in range(len(connected_components)):
        for j in range(len(connected_components[i])):
            print(connected_components[i][j], end = " ")
        print("")


    # Write results into results.txt
    with open("examples/TestData/Results.txt", 'w') as filehandle:
        for color in connected_components:
            for i in range(len(color)):
                if i==len(color)-1: filehandle.write('%d\n' % color[i])
                else: filehandle.write('%d ' % color[i])
