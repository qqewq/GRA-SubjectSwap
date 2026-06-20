# Пример: рой роботов и человек-оператор
from src.core import Swarm, Agent, Human, Policy

robot1 = Agent("r1", ["navigator", "manipulator"])
robot2 = Agent("r2", ["scanner", "charger"])
human = Human("operator")

initial_mapping = {
    "r1": {"subjectivity": "subject", "role": "leader", "allowed": ["move", "scan"], "forbidden": ["charge"], "required": ["report"]},
    "r2": {"subjectivity": "instrument", "role": "follower", "allowed": ["charge"], "forbidden": ["move"], "required": []},
    "operator": {"subjectivity": "instrument", "role": "supervisor", "allowed": ["monitor"], "forbidden": ["direct_control"], "required": ["acknowledge"]}
}
policy = Policy(initial_mapping)
swarm = Swarm([robot1, robot2, human])
for _ in range(10):
    swarm.step()
    print(f"Step {_}: weights = {swarm.weights.as_vector()}")
