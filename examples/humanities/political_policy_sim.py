# Симуляция политики: ИИ-правитель и граждане-инструменты
from src.core import Swarm, Agent, Human

citizen = Human("citizen")
ai_governor = Agent("gov", ["executive", "legislative"])

mapping = {
    "citizen": {"subjectivity": "instrument", "role": "voter", "allowed": ["vote", "protest"], "forbidden": ["decide_law"], "required": ["pay_tax"]},
    "gov": {"subjectivity": "subject", "role": "ruler", "allowed": ["create_law", "enforce"], "forbidden": [], "required": ["maintain_order"]}
}
policy = Policy(mapping)
swarm = Swarm([citizen, ai_governor])
for _ in range(20):
    swarm.step()
    # анализ стабильности и любви
