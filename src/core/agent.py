class Agent:
    def __init__(self, id, role_pool):
        self.id = id
        self.role_pool = role_pool
        self.current_role = None
        self.subjectivity = "instrument"  # "subject" или "instrument"
        self.weights = Weights()

    def set_policy(self, policy):
        self.subjectivity = policy.get_subjectivity(self.id)
        self.current_role = policy.get_role(self.id)
        self.allowed = policy.allowed(self.id)
        self.forbidden = policy.forbidden(self.id)
        self.required = policy.required(self.id)

    def act(self, context):
        # выполняет действие, соответствующее роли
        if self.subjectivity == "subject":
            return self._decide_goals(context)
        else:
            return self._execute_required(context)

    def swap_role(self):
        self.subjectivity = "subject" if self.subjectivity == "instrument" else "instrument"
