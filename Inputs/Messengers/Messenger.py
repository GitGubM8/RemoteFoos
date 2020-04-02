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
	_newMessageTrigger = ParamedEvent()
	@property
	def NewMessageEvent(self) -> ParamedEvent_IReadOnly:
		return self._newMessageTrigger

	def Announce(self, message: Message) -> None:
		self._newMessageTrigger.Publish(message)
	
	def _WipeDispatchers(self):
		del self._newMessageTrigger
		
		super(Messenger, self)._WipeDispatchers()