"""Контур с участием человека через CLI."""
import sys
sys.path.insert(0, "src")
from gra_subjectswap.optimus.env import OptimusEnv
from gra_subjectswap.optimus.robot_policy_optimus import OptimusRobotPolicy, DummyRobotModel
from gra_subjectswap.core.swap_engine import SubjectSwapEngine
from gra_subjectswap.core.subject_state import SubjectState, SubjectWeights
from gra_subjectswap.core.roles import RoleType
from gra_subjectswap.core.gra_nullifier import GRANullifier
from gra_subjectswap.core.policies import HumanPolicy

class CLIHumanPolicy(HumanPolicy):
    def act(self, state):
        print("Текущее состояние робота:", state)
        delta = input("Введите object_delta через пробел (x y z): ")
        vals = [float(x) for x in delta.split()]
        action = {"object_delta": vals}
        return super().act({**state, "human_input": action})

env = OptimusEnv()
human_pol = CLIHumanPolicy(allowed={"object_delta"}, forbidden=set(), required={"object_delta"})
robot_pol = OptimusRobotPolicy(DummyRobotModel())
nullifier = GRANullifier()
state = SubjectState(RoleType.INSTRUMENT, RoleType.SUBJECT, SubjectWeights())
engine = SubjectSwapEngine(human_pol, robot_pol, nullifier, state)

for t in range(10):
    obs = env.get_state()
    out = engine.step(obs)
    env.apply_robot_action(out["agent_action"])
    env.apply_human_action(out["human_action"])
    print(f"Step {t}: {out['roles']}")
    if t % 3 == 0:
        engine.swap()
