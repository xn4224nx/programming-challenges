#!/usr/bin/python3
"""
GENERATE GRAPHICAL EDITOR SAMPLES
=================================

Create a number of random graphical editor sample files and the final 
output they would create.
"""

import numpy as np

MAX_HEIGHT = 250

class GraphEditor:
	def __init__(self, width, height):
		self.width_m = width
		self.height_n = height
		
		# Create the blank image
		self.image = np.zero((self.height_n, self.width_m))
		
		# Create the set of instructions that are fed to the editor
		self.instructions = [f"I {str(self.width_m)} {str(self.height_n)}"]
		
	def clear(self):
		"""
		Wipe the image and set every value in the array to white.
		"""
		self.image.fill(0)
		self.instructions.append("C")
		
	def paint_pixel(self, width_p, height_p, colour):
		"""
		Colour the pixel indicated by the coordinate to the given colour.
		"""
		self.image[height_p, width_p] = colour
		self.instructions.append(f"L {width_p} {height_p} {colour}")
			
	def vert_paint(self, width_p, height_0, height_1, colour):
		"""
		Paint a vertical column in the image a particular colour.
		"""
		self.image[height_0:height_1 + 1, width_p] = colour
		self.instructions.append(f"V {width_p} {height_0} {height_1} {colour}")
		
	def horiz_paint(self, width_0, width_1, height_p, colour):
		"""
		Paint a horizonal row in the image a particular colour.
		"""
		self.image[height_p, width_0:width_1 + 1] = colour
		self.instructions.append(f"H {width_0} {width_1} {height_p} {colour}")
		
	def rect_paint(self, width_0, width_1, height_0, height_1, colour);
		"""
		Paint a rectangle in the image a particular colour.
		"""
		self.image[height_0:height_1 + 1, width_0:width_1 + 1] = colour
		self.instructions.append(f"K {width_0} {width_1} {height_0} {height_1} {colour}")
		
	def fill(self):
		pass
		
	def save(self):
		pass
		
	def exit_sess(self):
		pass
		
	
if __name__ == "__main__":
	img0 = GraphEditor(36, 36)
