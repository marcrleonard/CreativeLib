# this should mirror what is available in an svg
from ..enviornment.Canvas import Canvas

class BaseShape(object):
	def __init__(self, **kwargs):
		self._verticies = []
		self._fill_color='none'
		self._stroke_color='black'
		self._stroke_width=1
		self._close_path = False

		self.is_circle=False

		for k,v in kwargs.items():
			if hasattr(self, k):
				setattr(self, k, v)
			else:
				print(f'attr "{k}" does not exist.')

		Canvas.draw_queue.append(self)


	def __str__(self):
		return f'<{__class__} fill_color: {self.fill_color}>'

	def __repr__(self):
		return f'<{__class__} fill_color: {self.fill_color}>'

	@property
	def fill_color(self):
		return self._fill_color

	@fill_color.setter
	def fill_color(self, v):
		self._fill_color = v


	@property
	def close_path(self):
		return self._close_path

	@close_path.setter
	def close_path(self, v:bool):
		self._close_path = v


	@property
	def stroke_color(self):
		return self._stroke_color

	@stroke_color.setter
	def stroke_color(self, v):
		self._stroke_color = v

	@property
	def stroke_width(self):
		return self._stroke_width

	@stroke_width.setter
	def stroke_width(self, v):
		self._stroke_width = v

	@property
	def verticies(self):
		return self._verticies


	def add_vertex(self, coords:tuple):
		self._verticies.append(coords)


	def translate(self, x, y):
		# THIS IS DEFAULT BEHAVIOR IF IT IS NOT OVERRIDEN IN THE DERIVED CLASS.
		# This will work for shapes/objects that user vertex's.. but not for things like Circles

		for idx, (o_x,o_y) in enumerate(self._verticies):
			o_x = o_x + x
			o_y = o_y + y

			self._verticies[idx] = (o_x, o_y)

	def rotate(self, degrees, origin=None):
		raise Exception('Inherited class should implement')