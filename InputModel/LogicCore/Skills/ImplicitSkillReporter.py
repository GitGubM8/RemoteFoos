from InputModel.LogicCore.Skills.SkillReporter import *

class ImplicitSkillReporter_IReadOnly(SkillReporter_IReadOnly):
	pass
class ImplicitSkillReporter_IWriteOnly(SkillReporter_IWriteOnly):
	pass
class ImplicitSkillReporter_IReadWrite(SkillReporter_IReadWrite, ImplicitSkillReporter_IReadOnly, ImplicitSkillReporter_IWriteOnly):
	pass

class ImplicitSkillReporter(GarbageCollectableObject, ImplicitSkillReporter_IReadWrite):
	_skillUsedTrigger = Event()
	@property
	def SkillUsedEvent(self) -> Event_IReadOnly:
		return self._skillUsedTrigger

	def Execute(self) -> None:
		self._skillUsedTrigger.Publish()

	def _WipeDispatchers(self):
		del self._skillUsedTrigger

		super(ImplicitSkillReporter, self)._WipeDispatchers()