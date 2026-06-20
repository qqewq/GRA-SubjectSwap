# Интерактивная инсталляция: зритель — инструмент, ИИ — художник
from src.core import Swarm, Agent, Human

viewer = Human("viewer")
ai_artist = Agent("artist", ["composer", "performer"])

mapping = {
    "viewer": {"subjectivity": "instrument", "role": "canvas", "allowed": ["move", "stay"], "forbidden": ["speak"], "required": ["breathe"]},
    "artist": {"subjectivity": "subject", "role": "creator", "allowed": ["generate_visuals", "change_light"], "forbidden": [], "required": ["respond_to_movement"]}
}
policy = Policy(mapping)
swarm = Swarm([viewer, ai_artist])

while True:
    swarm.step()
    # на основе движений зрителя ИИ меняет проекции
