from abc import ABCMeta, abstractmethod
from sdv.domain.documents.actor_document import ActorDocument


class AbstractActorEntity(metaclass=ABCMeta):
    @abstractmethod
    def to_document(self) -> ActorDocument:
        raise NotImplementedError
