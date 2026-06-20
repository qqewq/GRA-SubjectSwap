class Human:
    def __init__(self, id):
        self.id = id
        self.subjectivity = "instrument"
        self.allowed = []
        self.forbidden = []
        self.required = []

    def set_policy(self, policy):
        self.subjectivity = policy.get_subjectivity(self.id)
        self.allowed = policy.allowed(self.id)
        self.forbidden = policy.forbidden(self.id)
        self.required = policy.required(self.id)

    def act(self, input_signal):
        # человек выполняет только разрешённые действия
        action = self._choose_from_allowed(input_signal)
        if action in self.required:
            return action
        if action in self.forbidden:
            raise ForbiddenActionError
        return action
