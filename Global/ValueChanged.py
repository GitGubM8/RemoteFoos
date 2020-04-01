class ValueChanged:
	_from = None
	@property
	def From(self):
		return self._from

	_to = None
	@property
	def To(self):
		return self._to

	def __init__(self, fromValue, toValue):
		self._from = fromValue
		self._to = toValue