import numpy as np

def read_csv(csv_path):
    """Read a CSV file and return a list of paths."""
    np_path_XYs = np.genfromtxt(csv_path, delimiter=',')
    path_XYs = []

    for i in np.unique(np_path_XYs[:, 0]):
        npXYs = np_path_XYs[np_path_XYs[:, 0] == i][:, 1:]
        XYs = []

        for j in np.unique(npXYs[:, 0]):
            XY = npXYs[npXYs[:, 0] == j][:, 1:]
            XYs.append(XY)

        path_XYs.append(XYs)
    
    return path_XYs

def write_csv(paths_XYs, csv_path):
    """Write a list of paths to a CSV file."""
    with open(csv_path, 'w') as f:
        for i, XYs in enumerate(paths_XYs):
            for XY in XYs:
                for j, point in enumerate(XY):
                    f.write(f"{i},{j},{point[0]},{point[1]}\n")

def regularize_paths(paths_XYs):
    """Regularize the paths by removing duplicate points."""
    regularized_paths = []
    
    for XYs in paths_XYs:
        regularized_XYs = []
        for XY in XYs:
            if len(XY) > 1:
                unique_XY = np.unique(XY, axis=0)
                regularized_XYs.append(unique_XY)
            else:
                regularized_XYs.append(XY)
        regularized_paths.append(regularized_XYs)
    
    return regularized_paths

def main(input_csv, output_csv):
    # Read the input CSV file
    paths_XYs = read_csv(input_csv)
    
    # Regularize the paths (remove duplicate points)
    regularized_paths_XYs = regularize_paths(paths_XYs)
    
    # Write the regularized paths to the output CSV file
    write_csv(regularized_paths_XYs, output_csv)

# Paths to the input and output CSV files
input_csv_path = 'resources/frag1.csv'
output_csv_path = 'out/frag01_sol.csv'

# Run the main function
main(input_csv_path, output_csv_path)
