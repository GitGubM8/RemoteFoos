from Global.GarbageCollectableObject import *

class Event_IReadOnly(IDisposedStatus):
	def Subscribe(self, callback) -> None:
		pass
	def Unsubscribe(self, callback) -> None:
		pass
class Event_IWriteOnly:
	def Publish(self) -> None:
		pass
class Event_IReadWrite(Event_IReadOnly, Event_IWriteOnly):
	pass

class ParamedEvent_IReadOnly(Event_IReadOnly):
	pass
class ParamedEvent_IWriteOnly:
	def Publish(self, value) -> None:
		pass
class ParamedEvent_IReadWrite(ParamedEvent_IReadOnly, ParamedEvent_IWriteOnly):
	pass

class Event(GarbageCollectableObject, Event_IReadWrite):
	def Subscribe(self, callback) -> None:
		assert callable(callback)
		self._listeners.add(callback)
	def Unsubscribe(self, callback) -> None:
		self._listeners.remove(callback)

	def Publish(self) -> None:
		assert self._isExecuting == False

		self._isExecuting = True
		for listener in self._listeners:
			try:
				listener()
			except:
				self._isExecuting = False
				raise
		self._isExecuting = False

	def __init__(self):
		super().__init__()
		self._listeners = set()
		self._isExecuting = False

	def _WipeDispatchers(self):
		self._listeners = None
	def _DisposeChildren(self):
		self._isExecuting = False
class ParamedEvent(GarbageCollectableObject, ParamedEvent_IReadWrite):
	def Subscribe(self, callback) -> None:
		self._listeners.add(callback)
	def Unsubscribe(self, callback) -> None:
		self._listeners.remove(callback)

	def Publish(self, value) -> None:
		assert self._isExecuting == False

		self._isExecuting = True
		for listener in self._listeners:
			try:
				listener(value)
			except TypeError:
				listener()
			else:
				self._isExecuting = False
		self._isExecuting = False

	def __init__(self):
		super().__init__()
		self._listeners = set()
		self._isExecuting = False

	def _WipeDispatchers(self):
		self._listeners = None
	def _DisposeChildren(self):
		self._isExecuting = False