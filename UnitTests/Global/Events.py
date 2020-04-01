import unittest

from Global.Events import *

class EventTest(unittest.TestCase):
    _fakeEvent = None
    _fakeParamedEvent = None

    def setUp(self) -> None:
        self._fakeEvent = Event()
        self._fakeParamedEvent = ParamedEvent()

    def tearDown(self) -> None:
        self._fakeEvent = None
        self._fakeParamedEvent = None

    def test_ParamlessEvent_Publish_ListenersAreCalled(self) -> None:
        callbackCount = 0
        def StubCallback():
            nonlocal callbackCount
            callbackCount += 1

        self._fakeEvent.Subscribe(StubCallback)

        self.assertEqual(0, callbackCount)

        self._fakeEvent.Publish()

        self.assertEqual(1, callbackCount)

    def test_ParamedEvent_Publish_ListenersAreCalled(self) -> None:
        callbackValue = None

        def StubCallback(value):
            nonlocal callbackValue
            callbackValue = value

        self._fakeParamedEvent.Subscribe(StubCallback)

        self.assertEqual(None, callbackValue)

        stubMessage = "stub_message"
        self._fakeParamedEvent.Publish(stubMessage)

        self.assertEqual(stubMessage, callbackValue)

if __name__ == '__main__':
    unittest.main()