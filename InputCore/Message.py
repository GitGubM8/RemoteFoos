from datetime import datetime

class Message:
	@property
	def WorkPlace(self) -> str:
		return self._workplace
	@property
	def Channel(self) -> str:
		return self._channel
	@property
	def Sender(self) -> str:
		return self._sender
	@property
	def Content(self) -> str:
		return self._content
	@property
	def TimeStamp(self) -> datetime:
		return self._timestamp

	def __init__(self, workplace: str, channel: str, sender: str, content: str, timestamp: datetime):
		self._workplace = workplace
		self._channel = channel
		self._sender = sender
		self._content = content
		self._timestamp = timestamp