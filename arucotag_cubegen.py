import cv2
import numpy as np

camera_matrix = np.array([[640, 0, 320], [0, 640, 240], [0, 0, 1]], dtype=np.float32)

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_100)
aruco_params = cv2.aruco.DetectorParameters_create()

cube_vertices = np.array([
                          [0.03, -0.03, 0.06],
                          [0.03, 0.03, 0.06],
                          [-0.03, 0.03, 0.06],
                          [-0.03, -0.03, 0.06],
                          [0.03, -0.03, 0],
                          [0.03, 0.03, 0],
                          [-0.03, 0.03, 0],
                          [-0.03, -0.03, 0]])

cube_edges = [(0, 1), (1, 2), (2, 3), (3, 0),
              (4, 5), (5, 6), (6, 7), (7, 4),
              (0, 4), (1, 5), (2, 6), (3, 7)]

# Main AR loop
def cube_on_aruco():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        corners, ids, _ = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=aruco_params)

        if ids is not None:
            for i in range(len(ids)):
                rot_mat, trans_vec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.05, camera_matrix, None)
                rotation = rot_mat[0]
                translation = trans_vec[0]

                cube_points, _ = cv2.projectPoints(cube_vertices, rotation, translation, camera_matrix, None)

                for edge in cube_edges:
                    start = tuple(map(int, cube_points[edge[0]].ravel()))
                    end = tuple(map(int, cube_points[edge[1]].ravel()))
                    cv2.line(frame, start, end, (255, 255, 0), 2)

        cv2.imshow("AR Cube", frame)

        key = cv2.waitKey(1)
        if key == 27:  # Press Esc key to exit
            break



    cap.release()
    cv2.destroyAllWindows()

print("Drawing 3D cube on aruco marker")
cube_on_aruco()
