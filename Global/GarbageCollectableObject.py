class IDisposedStatus:
	def IsDisposed(self) -> bool:
		pass

class GarbageCollectableObject(IDisposedStatus):
	_isDisposed = False
	@property
	def IsDisposed(self) -> bool:
		return self._isDisposed

	def _RemoveListeners(self):
		pass
	def _DisposeChildren(self):
		pass
	def _OstracizeParent(self):
		pass
	def _WipeDispatchers(self):
		pass

	def __del__(self):
		if (self._isDisposed):
			return
		self._isDisposed = True

		self._RemoveListeners()
		self._DisposeChildren()
		self._OstracizeParent()
		self._WipeDispatchers()