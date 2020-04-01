from Global.Events import *

class PossessionReporter_IReadOnly:
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

class PossessionReporter(PossessionReporter_IReadWrite):
	_hasPossession = False
	@property
	def HasPossession(self):
		return self._hasPossession

	_possessionGainedTrigger = Event()
	@property
	def PossessionGainedEvent(self) -> Event_IReadOnly:
		return self._possessionGainedTrigger
	def GrantPossession(self) -> None:
		if (self._hasPossession):
			return
		self._hasPossession = True
		self._possessionGainedTrigger.Publish()

	_possessionLostTrigger = Event()
	@property
	def PossessionLostEvent(self) -> Event_IReadOnly:
		return self._possessionLostTrigger
	def RemovePossession(self) -> None:
		if (self._hasPossession == False):
			return
		self._hasPossession = False
		self._possessionLostTrigger.Publish()