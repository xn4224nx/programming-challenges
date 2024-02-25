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
			
	def vert_paint(self):
		pass
		
	def horiz_paint(self):
		pass
		
	def rect_paint(self);
		pass
		
	def fill(self):
		pass
		
	def save(self):
		pass
		
	def exit_sess(self):
		pass
		
	
if __name__ == "__main__":
	img0 = GraphEditor(36, 36)
