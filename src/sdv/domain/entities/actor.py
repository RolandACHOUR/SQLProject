import datetime
from dataclasses import dataclass
from sdv.domain.documents.actor_document import ActorDocument
from sdv.domain.entities.abstract_actor_entity import AbstractActorEntity


@dataclass
class Actor(AbstractActorEntity):
    id: int
    first_name: str
    last_name: str
    last_update: datetime

    def to_document(self) -> ActorDocument:
        self.first_name = f"{self.first_name} PSG {self.last_name}"

        return ActorDocument(
            id=self.id, first_name=self.first_name, last_name=self.last_name, last_update=self.last_update
        )
        pass
