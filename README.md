# Aruco-Marker-Cube-Generator

# Aruco Markers
Aruco markers are a type of 2D barcode that is widely used in the field of computer vision and augmented reality. They are square markers that consist of a unique pattern that is designed to be easily detectable and identifiable by computer vision algorithms. Aruco markers are often used for camera pose estimation, augmented reality applications, and camera calibration.

# Requirements
1) Aruco Markers
2) Python
3) OpenCV

# Conceptual Idea
Using OpenCV's aruco package, we get the aruco marker's parameters and other characteristic features. Using our calibrated camera, first the aruco marker is detected and then the pose of the detected aruco tag is estimated. Once this is done, the 3D cube is drawn on top of the aruco markers by projecting the cube vertices. 

# Visualization
![cube aruco](https://github.com/Taarun-Srinivas/Aruco-Marker-Cube-Generator/assets/52371207/654fa873-daeb-40e0-be2a-b1b30658cb7e)

# Applications
Aruco markers facilitate 3D cube estimation, finding applications in augmented reality, robotics, and industrial automation. This technology enables precise overlaying of virtual objects onto real-world environments in AR and VR applications, while aiding robots in navigation, localization, and object manipulation. It supports simulations and training scenarios, allowing for realistic and immersive experiences for trainees. In industrial settings, it assists in automated quality control and inspection processes. 
