import abc


class AlarmBackend(abc.ABC):
    @abc.abstractmethod
    def fire(self, alarm):
        pass

    @abc.abstractmethod
    def publish(self, alarm):
        pass

    @abc.abstractmethod
    def remove(self, alarm):
        pass

    @abc.abstractmethod
    def snooze(self, alarm):
        pass

    @abc.abstractmethod
    def stop(self, alarm):
        pass
