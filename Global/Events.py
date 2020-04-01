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

    def Subscribe(self, callback) -> None:
        self._listeners.add(callback)

    def Unsubscribe(self, callback) -> None:
        self._listeners.remove(callback)

    def Publish(self) -> None:
        for listener in self._listeners:
            listener()

class ParamedEvent(ISubscriber, IParamedPublisher):
    _listeners = set()

    def Subscribe(self, callback) -> None:
        self._listeners.add(callback)

    def Unsubscribe(self, callback) -> None:
        self._listeners.remove(callback)

    def Publish(self, value) -> None:
        for listener in self._listeners:
            listener(value)