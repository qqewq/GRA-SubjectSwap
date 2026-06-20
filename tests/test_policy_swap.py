def test_policy_swap():
    policy = Policy({"a": {"subjectivity": "subject", "role": "X"}, "b": {"subjectivity": "instrument", "role": "Y"}})
    swapped = policy.swap()
    assert swapped.get_subjectivity("a") == "instrument"
    assert swapped.get_subjectivity("b") == "subject"
    # роли также изменились
