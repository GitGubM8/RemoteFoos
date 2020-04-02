from Global.Events import *

class SkillReporter_IReadOnly(IDisposedStatus):
	@property
	def SkillUsedEvent(self) -> Event_IReadOnly:
		pass
class SkillReporter_IWriteOnly:
	def Execute(self) -> None:
		pass
class SkillReporter_IReadWrite(SkillReporter_IReadOnly, SkillReporter_IWriteOnly):
	pass