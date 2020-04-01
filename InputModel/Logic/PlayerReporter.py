class PlayerReporter_IReadOnly:
	pass
class PlayerReporter_IWriteOnly:
	pass
class PlayerReporter_IReadWrite(PlayerReporter_IReadOnly, PlayerReporter_IWriteOnly):
	pass

class PlayerReporter(PlayerReporter_IReadWrite):
	pass