from sqlalchemy.orm import declarative_base
from actor_sql import ActorSQL

Base = declarative_base()

ActorSQL(Base)
