class KeyValuePair:
	@property
	def Key(self):
		return self._key
	@property
	def Value(self):
		return self._value

	def __init__(self, key, value):
		self._key = key
		self._value = value