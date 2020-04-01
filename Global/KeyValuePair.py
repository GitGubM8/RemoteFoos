class KeyValuePair:
	_key = None
	@property
	def Key(self):
		return self._key

	_value = None
	@property
	def Value(self):
		return self._value

	def __init__(self, key, value):
		self._key = key
		self._value = value