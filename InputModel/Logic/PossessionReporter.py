from Global.Events import *

class PossessionReporter_IReadOnly(IDisposedStatus):
	@property
	def HasPossession(self) -> bool:
		pass
	@property
	def PossessionGainedEvent(self) -> Event_IReadOnly:
		pass
	@property
	def PossessionLostEvent(self) -> Event_IReadOnly:
		pass
class PossessionReporter_IWriteOnly:
	def GrantPossession(self) -> None:
		pass
	def RemovePossession(self) -> None:
		pass
class PossessionReporter_IReadWrite(PossessionReporter_IReadOnly, PossessionReporter_IWriteOnly):
	pass

class PossessionReporter(GarbageCollectableObject, PossessionReporter_IReadWrite):
	@property
	def HasPossession(self):
		return self._hasPossession

	@property
	def PossessionGainedEvent(self) -> Event_IReadOnly:
		return self._possessionGainedTrigger
	def GrantPossession(self) -> None:
		if (self._hasPossession):
			return
		self._hasPossession = True
		self._possessionGainedTrigger.Publish()

	@property
	def PossessionLostEvent(self) -> Event_IReadOnly:
		return self._possessionLostTrigger
	def RemovePossession(self) -> None:
		if (self._hasPossession == False):
			return
		self._hasPossession = False
		self._possessionLostTrigger.Publish()

	def __init__(self):
		super().__init__()
		self._hasPossession = False
		self._possessionGainedTrigger = Event()
		self._possessionLostTrigger = Event()

	def _WipeDispatchers(self):
		del self._possessionGainedTrigger
		del self._possessionLostTrigger

		super()._WipeDispatchers()