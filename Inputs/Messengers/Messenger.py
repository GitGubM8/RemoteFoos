from Global.Events import *

from InputCore.Message import Message

class Messenger_IReadOnly:
	@property
	def NewMessageEvent(self) -> ParamedEvent_IReadOnly:
		pass
class Messenger_IWriteOnly:
	def Announce(self, message: Message) -> None:
		pass
class Messenger_IReadWrite(Messenger_IReadOnly, Messenger_IWriteOnly):
	pass

class Messenger(Messenger_IReadWrite):
	_newMessageTrigger = ParamedEvent()
	@property
	def NewMessageEvent(self) -> ParamedEvent_IReadOnly:
		return self._newMessageTrigger

	def Announce(self, message: Message) -> None:
		self._newMessageTrigger.Publish(message)