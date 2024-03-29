#!/usr/bin/python3
"""
GENERATE GRAPHICAL EDITOR SAMPLES
=================================

Create a number of random graphical editor sample files and the final 
output they would create.
"""

import numpy as np
import random

MAX_HEIGHT = 250
MAX_COLOUR = 256*256*256

class GraphEditor:
	def __init__(self, width, height):
		self.width_m = width
		self.height_n = height
		
		# Create the blank image
		self.image = np.zeros((self.height_n, self.width_m))
		
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
		
	def rect_paint(self, width_0, width_1, height_0, height_1, colour):
		"""
		Paint a rectangle in the image a particular colour.
		"""
		self.image[height_0:height_1 + 1, width_0:width_1 + 1] = colour
		self.instructions.append(f"K {width_0} {width_1} {height_0} {height_1} {colour}")
		
	def fill(self, width_p, height_p, colour):
		"""
		Fill a region of the image which has the same colour with a new
		colour. Then fill every connected pixel that has the same 
		original colour with the new colour.
		
		Connected is defined as being above, below, left or right of the
		original pixel.
		"""
		
		orig_colour = self.image[height_p, width_p]
		adj_pixels = self.adj_pixels(width_p, height_p)

		while adj_pixels:
			
			new_adj_pixels = []
			
			for pixel in adj_pixels:
				
				# Check if the pixel is the original colour
				if self.image[pixel[1], pixel[0]] == orig_colour:
					
					# Change the pixels colour to the new colour
					self.image[pixel[1], pixel[0]] = colour
					
					# Save the new adjacent pixels for this pixel
					new_adj_pixels += self.adj_pixels(pixel[0], pixel[1])
					
			adj_pixels = new_adj_pixels
		
		self.instructions.append(f"F {width_p} {height_p} {colour}")
	
	def save(self, filename):
		"""
		Save the file
		"""
		self.instructions.append(f"S {filename}")
		np.savetxt(filename, self.image, fmt='%7d', 
					delimiter=' ', newline='\n', 
					header='', footer='', 
					comments='# ', encoding=None)
			
	def exit_sess(self):
		"""
		End the session
		"""
		self.instructions.append(f"X")
		
	def adj_pixels(self, width_p, height_p) -> list:
		"""
		Find all the adjacent pixels to the original pixel.
		"""
		
		adj_pixels = []
			
		# Vertical
		if height_p > 0:
			adj_pixels.append((width_p, height_p - 1))
		
		if height_p < self.height_n - 1:
			adj_pixels.append((width_p, height_p + 1))

		# Horizontal
		if width_p > 0:
			adj_pixels.append((width_p - 1, height_p))
		
		if width_p < self.width_m - 1:
			adj_pixels.append((width_p + 1, height_p))
		
		return adj_pixels

	def save_inst(self, filepath: str):
		"""
		Save a text file that contains all the instructions that were
		used by the class.
		"""
		
		all_commands = "\n".join(self.instructions)
		
		with open(filepath, "w") as fp:
			fp.write(all_commands)
	
	def rnd_colour(self) -> int:
		"""
		Return a random colour value that is compatible with the editor.
		"""
		return random.randrange(MAX_COLOUR)

	def rnd_rect(self) -> (int, int, int, int):
		"""
		Generate the height and width values for two coordinate points
		that define a rectangle that fits completely in the image.
		"""
		
		width_0 = random.randrange(self.width_m - 1)
		width_1 = random.randrange(width_0, self.width_m)
		
		height_0 = random.randrange(self.height_n - 1)
		height_1 = random.randrange(height_0, self.height_n)
		
		return (width_0, width_1, height_0, height_1)

		
if __name__ == "__main__":
	
	# Generate a set number of instruction files and their outputs
	for idx in range(100):
		
		# Generate the image size
		width = random.randrange(10, MAX_HEIGHT + 1)
		height = random.randrange(10, width + 1)
		
		# Generate the image command
		img = GraphEditor(width, height)
		
		# A random number of functions
		num_commands = random.randrange(3, 13)
		
		for _ in range(num_commands):
			
			# Select a random function
			command = random.randrange(6)
			
			# Generate a colour & rectangle for use in the command
			rcolour = img.rnd_colour()
			rrect = img.rnd_rect()
			
			if command == 0:
				img.clear()
			
			elif command == 1:
				img.paint_pixel(rrect[0], rrect[2], rcolour)
			
			elif command == 2:
				img.vert_paint(rrect[0], rrect[2], rrect[3], rcolour)
			
			elif command == 3:
				img.horiz_paint(rrect[0], rrect[1], rrect[2], rcolour)
			
			elif command == 4:
				img.rect_paint(rrect[0], rrect[1], rrect[2], rrect[3], rcolour)
			
			elif command == 5:
				img.fill(rrect[0], rrect[2], rcolour)
			
		# Save the image before exit
		img.save(f"data/image_{idx:02d}.bmp")
		
		# Terminate the session
		img.exit_sess()
		
		# Save the instruction file
		img.save_inst(f"data/instruction_{idx:02d}.txt")
				
		print(f"Image & Instruction set {idx:02d} created.")
