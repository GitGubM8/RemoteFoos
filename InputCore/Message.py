from datetime import datetime

class Message:
	_workplace = None
	@property
	def WorkPlace(self) -> str:
		return self._workplace

	_channel = None
	@property
	def Channel(self) -> str:
		return self._channel

	_sender = None
	@property
	def Sender(self) -> str:
		return self._sender

	_content = None
	@property
	def Content(self) -> str:
		return self._content

	_timestamp = None
	@property
	def TimeStamp(self) -> datetime:
		return self._timestamp

	def __init__(self, workplace: str, channel: str, sender: str, content: str, timestamp: datetime):
		self._workplace = workplace
		self._channel = channel
		self._sender = sender
		self._content = content
		self._timestamp = timestamp