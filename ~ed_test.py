#test file for the edge detection

import cv2
import numpy as np
import matplotlib.pyplot as plt
import v

def edges_grayed():

	plt.imshow(v.image_edges, cmap='gray')
	plt.show()

#for an explanation of the Hough transform check https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
def edges_lined():
	rho = 1
	theta = np.pi/180
	threshold = 50
	min_line_length = 100
	max_line_gap = 5 

	lines = cv2.HoughLinesP(v.image_edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

	lined_image = np.copy(v.image_edges)

	for line in lines:
		for x1, y1, x2, y2 in line:
			cv2.line(lined_image, (x1,y1),(x2,y2), (255,0,0), 3, cv2.LINE_AA)

	plt.imshow(lined_image)
	plt.show()

edges_grayed()
edges_lined()