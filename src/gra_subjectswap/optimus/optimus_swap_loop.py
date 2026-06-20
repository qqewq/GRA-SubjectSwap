from .env import OptimusEnv
from .human_policy_optimus import OptimusHumanPolicy
from .robot_policy_optimus import OptimusRobotPolicy, DummyRobotModel
from ..core.swap_engine import SubjectSwapEngine
from ..core.subject_state import SubjectState, SubjectWeights
from ..core.roles import RoleType
from ..core.gra_nullifier import GRANullifier
from ..core.logging import SwapLogger

def run_optimus_subjectswap():
    env = OptimusEnv()
    human_policy = OptimusHumanPolicy(
        allowed={"object_delta"},
        forbidden={"joint_delta"},  # человек не может напрямую двигать суставы
        required={"object_delta"},
    )
    robot_model = DummyRobotModel()
    robot_policy = OptimusRobotPolicy(model=robot_model)
    nullifier = GRANullifier()
    logger = SwapLogger()  # можно передать файл

    state = SubjectState(
        human_role=RoleType.INSTRUMENT,
        agent_role=RoleType.SUBJECT,
        weights=SubjectWeights(),
    )
    engine = SubjectSwapEngine(human_policy, robot_policy, nullifier, state)

    obs = env.reset()
    for t in range(100):
        obs = env.get_state()
        out = engine.step(obs)
        env.apply_robot_action(out["agent_action"])
        env.apply_human_action(out["human_action"])
        logger.log_step(
            t, obs, out["human_action"], out["agent_action"],
            out["roles"], out["weights"]
        )
        if t % 20 == 0:
            engine.swap()
            print(f"Step {t}: Swapped roles. Now human is {state.human_role.name}, agent is {state.agent_role.name}")

    print("Final weights:", state.weights)
    return logger.records

if __name__ == "__main__":
    run_optimus_subjectswap()
