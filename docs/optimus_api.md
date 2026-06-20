# API модуля Optimus

## `OptimusEnv`
- `reset() -> state`
- `get_state() -> dict`
- `apply_robot_action(action)`
- `apply_human_action(action)`

## `HumanPolicyOptimus(allowed, forbidden, required)`
- `act(state) -> action`

## `RobotPolicyOptimus(model)`
- `act(state) -> action`

## `SubjectSwapEngine`
- `step(env_state) -> outputs`
- `swap()`
