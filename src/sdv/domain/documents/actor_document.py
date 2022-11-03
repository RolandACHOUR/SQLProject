from abc import abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import Dict
from sdv.domain.entities.actor import Actor
import datetime


@dataclass
class ActorDocument:
    id: int
    first_name: str
    last_name: str
    last_update: datetime
    tmp: str

    @abstractmethod
    def to_a_document(self, index_name: str = None, es_id: int = 1) -> Dict:
        return {
            "_index": index_name,
            "_id": es_id,
            "_op_type": "index",
            "_source": {
                "id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "last_update": self.last_update,
            }
        }


