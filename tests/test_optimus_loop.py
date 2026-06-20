from gra_subjectswap.optimus.optimus_swap_loop import run_optimus_subjectswap

def test_run_loop():
    records = run_optimus_subjectswap()
    assert len(records) == 100
    # проверяем, что свапы произошли (разные роли в логах)
    roles_set = {tuple(r["roles"].values()) for r in records}
    assert len(roles_set) >= 2
