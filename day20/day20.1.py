tiles = open('input.txt').read().split('\n\n')

class Tile():

	def __init__(self, id, image):
		self.id = id

		self.pic = image.split('\n')
		# from left to right, from top to bottom
		self.edge_e = ''
		self.edge_w = ''
		self.edge_n = self.pic[0][:]
		self.edge_s = self.pic[-1][:]
		for line in self.pic:
			self.edge_w += line[0]
			self.edge_e += line[-1]



	def get_opposite_direction(self, direction):
		if direction == 'e':
			return self.edge_w
		elif direction == 's':
			return self.edge_n
		elif direction == 'w':
			return self.edge_e
		else:
			return self.edge_s

	def get_direction(self, direction):
		if direction == 'e':
			return self.edge_e
		elif direction == 's':
			return self.edge_s
		elif direction == 'w':
			return self.edge_w
		else:
			return self.edge_n

	# turn anticlockwise
	def turn90(self):
		self.edge_n, self.edge_e, self.edge_s, self.edge_w = self.edge_e, self.edge_s[::-1], self.edge_w, self.edge_n[
																										  ::-1]

		new_img = []
		for pos in range(len(self.pic[0])):
			current_row = ''
			for row in self.pic:
				current_row += row[pos]
			new_img.insert(0, current_row)
		self.pic = new_img

	def flip_horizontal(self):
		self.edge_w, self.edge_e = self.edge_w[::-1], self.edge_e[::-1]
		self.edge_n, self.edge_s = self.edge_s, self.edge_n

		self.pic = self.pic[::-1]

	def __repr__(self):
		return str(self.id)

class Puzzle():

	def __init__(self):
		self.all_tiles = []
		self.whole_image = []

	def assemble(self):
		# take a tile
		starting_tile = self.all_tiles.pop(0)
		
		# go up
		self.move_up_down(starting_tile, 'n')

		# go down
		self.move_up_down(starting_tile, 's')
				

	def move_up_down(self, starting_tile, up_or_down):
		temp_tiles = self.all_tiles
		current_tile = starting_tile
		
		while current_tile is not None:
			current_row = [current_tile]

			# go right until tile is an edge
			while current_tile is not None:
				# find right piece for current tile
				current_tile = self.find_match(current_tile.edge_e, 'e', temp_tiles)
				if current_tile is not None:
					temp_tiles.remove(current_tile)
					current_row.append(current_tile)

			current_tile = starting_tile

			# go left until tile is an edge
			while current_tile is not None:
				# find right piece for current tile
				current_tile = self.find_match(current_tile.edge_w, 'w', temp_tiles)
				if current_tile is not None:
					temp_tiles.remove(current_tile)
					current_row.insert(0, current_tile)

			# add current row
			if len(current_row) != 1:
				if up_or_down == 'n':
					self.whole_image.insert(0, current_row)
				else:
					self.whole_image.append(current_row)

			# go one up/down 
			current_tile = self.find_match(starting_tile.get_direction(up_or_down), up_or_down, temp_tiles)
			starting_tile = current_tile
			if current_tile is not None:
				self.all_tiles.remove(current_tile)



	def find_match(sefl, edge, direction, pool):
		
		found = None
		for t in pool:
			for i in range(4):
				for j in range(2):
					if edge == t.get_opposite_direction(direction):
						return t
					t.flip_horizontal()
				t.turn90()

		return found


	def add_tile(self, tile):
		self.all_tiles.append(tile)


puzzle = Puzzle()
for tile in tiles:
	current_id = int(tile.split(':')[0].split(' ')[1])
	new_tile = Tile(current_id, tile.split(':')[1].strip())

	puzzle.add_tile(new_tile)

puzzle.assemble()
img = puzzle.whole_image
print(img[0][0].id * img[len(img)-1][0].id * img[0][len(img)-1].id * img[len(img)-1][len(img)-1].id)


