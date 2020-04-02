from Global.Events import *

from InputCore.Message import Message

class Messenger_IReadOnly(IDisposedStatus):
	@property
	def NewMessageEvent(self) -> ParamedEvent_IReadOnly:
		pass
class Messenger_IWriteOnly:
	def Announce(self, message: Message) -> None:
		pass
class Messenger_IReadWrite(Messenger_IReadOnly, Messenger_IWriteOnly):
	pass

class Messenger(GarbageCollectableObject, Messenger_IReadWrite):
	@property
	def NewMessageEvent(self) -> ParamedEvent_IReadOnly:
		return self._newMessageTrigger

	def Announce(self, message: Message) -> None:
		self._newMessageTrigger.Publish(message)

	def __init__(self):
		super().__init__()
		self._newMessageTrigger = ParamedEvent()

	def _WipeDispatchers(self):
		del self._newMessageTrigger
		super()._WipeDispatchers()