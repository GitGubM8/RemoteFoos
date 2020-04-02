class IDisposedStatus:
	def IsDisposed(self) -> bool:
		pass

class GarbageCollectableObject(IDisposedStatus):
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

	def __init__(self):
		self._isDisposed = False

	def __del__(self):
		if (self._isDisposed):
			return
		self._isDisposed = True

		self._RemoveListeners()
		self._DisposeChildren()
		self._OstracizeParent()
		self._WipeDispatchers()