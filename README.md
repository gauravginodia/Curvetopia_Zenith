# Curvetopia_Zenith

## Curve Regularization and Symmetry Detection

## Project Overview

This project is part of the Curvetopia initiative, which aims to identify, regularize, and evaluate symmetry in 2D curves represented as polylines. The process involves loading curve data from CSV files, analyzing the curves for regular geometric shapes and symmetry, fitting Bezier curves to the points, and visualizing the results.

## Steps Involved

### 1. Loading Curve Data
- Curves are stored in CSV files, where each file represents one or more polylines.
- Each polyline is a sequence of points in 2D space.

### 2. Regularization
- Identify regular geometric shapes like straight lines, circles, ellipses, rectangles, and regular polygons within the curves.
- Smooth the curves to make them more regular and symmetrical.

### 3. Symmetry Detection
- Explore symmetry in the curves by detecting reflection symmetries.
- Analyze the curves to find lines of symmetry and determine if the curve can be divided into mirrored halves.

### 4. Fitting Bezier Curves
- Transform the curve representation into a set of Bezier curves by fitting the points to cubic Bezier parameters.
- Maintain the smoothness and accuracy of the curve representation.

### 5. Visualization
- Visualize the curves using `matplotlib` for inspection and evaluation.
- Highlight symmetrical and regularized curves for comparison.

## Code Implementation

### 1. Loading CSV Data
# 
```
import numpy as np

def read_csv(csv_path):
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
```

## Usage

### 1. Prepare the Environment
- Ensure all necessary libraries (`numpy`, `matplotlib`, `scipy`, etc.) are installed.

### 2. Run the Code
- Execute the code in a Jupyter Notebook or Python script.
- Load your curve CSV files using the `read_csv` function.
- Detect symmetry and fit Bezier curves using the provided functions.
- Visualize the results.

### 3. Expected Results
- The output should include plots of the curves with identified symmetries.
- Bezier curves fitted to the symmetrical parts of the curves will be highlighted.

## Evaluation Metrics

- **Symmetry Detection Accuracy:** Measured by comparing the symmetry lines detected with the known geometric properties of the shapes.
- **Regularization Success:** Evaluated by how closely the fitted Bezier curves approximate the original polylines.

