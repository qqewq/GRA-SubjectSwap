from enum import Enum, auto

class RoleType(Enum):
    SUBJECT = auto()
    INSTRUMENT = auto()

class ActorType(Enum):
    HUMAN = auto()
    AGENT = auto()

class SwarmRole(Enum):
    TRAINER = auto()
    LEARNER = auto()
    CRITIC = auto()
    ORCHESTRATOR = auto()
