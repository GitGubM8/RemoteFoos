class ISubscriber:
    def Subscribe(self, callback) -> None:
        pass

    def Unsubscribe(self, callback) -> None:
        pass

class IPublisher:
    def Publish(self) -> None:
        pass
class IParamedPublisher:
    def Publish(self, value) -> None:
        pass


class Event(ISubscriber, IPublisher):
    _listeners = set()
    _isExecuting = False

    def Subscribe(self, callback) -> None:
        assert callable(callback)
        self._listeners.add(callback)

    def Unsubscribe(self, callback) -> None:
        self._listeners.remove(callback)

    def Publish(self) -> None:
        assert self._isExecuting == False

        self._isExecuting = True
        for listener in self._listeners:
            try:
                listener()
            except:
                self._isExecuting = False
                raise
        self._isExecuting = False
class ParamedEvent(ISubscriber, IParamedPublisher):
    _listeners = set()
    _isExecuting = False

    def Subscribe(self, callback) -> None:
        self._listeners.add(callback)

    def Unsubscribe(self, callback) -> None:
        self._listeners.remove(callback)

    def Publish(self, value) -> None:
        assert self._isExecuting == False

        self._isExecuting = True
        for listener in self._listeners:
            try:
                listener(value)
            except TypeError:
                listener()
            else:
                self._isExecuting = False
        self._isExecuting = False