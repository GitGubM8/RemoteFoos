from Global.ValueChanged import *
from Global.Events import *

from InputModel.Logic.Roles.Role import *

class RoleReporter_IReadOnly(IDisposedStatus):
	@property
	def CurrentRole(self) -> Role:
		pass
	@property
	def RoleChangedEvent(self) -> ParamedEvent_IReadOnly:
		pass
class RoleReporter_IWriteOnly:
	def ChangeRole(self, role: Role) -> None:
		pass
class RoleReporter_IReadWrite(RoleReporter_IReadOnly, RoleReporter_IWriteOnly):
	pass

class RoleReporter(GarbageCollectableObject, RoleReporter_IReadWrite):
	_currentRole = None
	@property
	def CurrentRole(self) -> Role:
		return self._currentRole

	_roleChangedTrigger = ParamedEvent()
	@property
	def RoleChangedEvent(self) -> ParamedEvent_IReadOnly:
		return self._roleChangedTrigger
	def ChangeRole(self, role: Role) -> None:
		if (self._currentRole == role):
			return

		oldRole = self._currentRole
		self._currentRole = role
		self._roleChangedTrigger.Publish(ValueChanged(oldRole, self._currentRole))

	def __init__(self, role: Role):
		self._currentRole = role

	def _WipeDispatchers(self):
		del self._roleChangedTrigger
		super(RoleReporter, self)._WipeDispatchers()
	def _DisposeChildren(self):
		self._currentRole = None
		super(RoleReporter, self)._DisposeChildren()