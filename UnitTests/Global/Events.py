import unittest

from Global.Events import *

class EventTest(unittest.TestCase):
	def setUp(self) -> None:
		self._fakeEvent = Event()
		self._fakeParamedEvent = ParamedEvent()

	def tearDown(self) -> None:
		del self._fakeEvent
		del self._fakeParamedEvent

	def test_ParamlessEvent_Publish_ListenersAreCalled(self) -> None:
		callbackCount = 0
		def StubCallback():
			nonlocal callbackCount
			callbackCount += 1
		self._fakeEvent.Subscribe(StubCallback)

		self.assertEqual(0, callbackCount)

		self._fakeEvent.Publish()

		self.assertEqual(1, callbackCount)

	def test_ParamedEvent_Publish_ParamedListenersAreCalled(self) -> None:
		callbackValue = None
		def StubCallback(value):
			nonlocal callbackValue
			callbackValue = value
		self._fakeParamedEvent.Subscribe(StubCallback)

		self.assertEqual(None, callbackValue)

		stubMessage = "stub_message"
		self._fakeParamedEvent.Publish(stubMessage)

		self.assertEqual(stubMessage, callbackValue)

	def test_ParamedEvent_Publish_UnparamedListenersAreCalled(self) -> None:
		callbackCount = 0
		def StubCallback():
			nonlocal callbackCount
			callbackCount += 1
		self._fakeParamedEvent.Subscribe(StubCallback)

		self.assertEqual(0, callbackCount)

		stubMessage = "stub_message"
		self._fakeParamedEvent.Publish(stubMessage)

		self.assertEqual(1, callbackCount)

	def test_Event_Cyclic_RaisesError(self) -> None:
		def PublishEvent():
			self._fakeEvent.Publish()
		self._fakeEvent.Subscribe(PublishEvent)

		self.assertRaises(AssertionError, PublishEvent)

if __name__ == '__main__':
	unittest.main()