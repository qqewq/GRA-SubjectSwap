from gra_subjectswap.core.roles import RoleType, SwarmRole

def test_role_types():
    assert RoleType.SUBJECT != RoleType.INSTRUMENT

def test_swarm_roles():
    assert SwarmRole.TRAINER.value != SwarmRole.LEARNER.value
